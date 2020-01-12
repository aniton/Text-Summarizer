from flask import Flask, request, jsonify, render_template
from summary import model
import json
import os


from opencensus.ext.stackdriver import trace_exporter as stackdriver_exporter
import opencensus.trace.tracer

def initialize_tracer():
    project_id = os.environ['GCLOUD_PROJECT']
    exporter = stackdriver_exporter.StackdriverExporter(
        project_id=project_id
    )
    tracer = opencensus.trace.tracer.Tracer(
        exporter=exporter,
        sampler=opencensus.trace.tracer.samplers.AlwaysOnSampler()
    )

    return tracer

app = Flask(__name__)


@app.route('/')
def home():
    return 'Text summarizer service. Please use /summarize'


@app.route('/health')
def health():
    tracer = app.config['TRACER']
    tracer.start_span(name='health')
    
    result = "Tracing requests"
    tracer.end_span()
    return 'alive', 200#,  requests


@app.route('/summarize', methods=['POST'])
def predict():
    project_id = os.environ['GCLOUD_PROJECT']

    tracer = initialize_tracer()

    tracer = app.config['TRACER']
    tracer.start_span(name='summarize')

    text = request.get_data()
    topic = request.args.get('topic')

    # if not topic:
    #     return jsonify({"error": "no topic present"}), 400
    if not text.strip():
        return jsonify({"error": "empty text"}), 400

    summary, accuracy = model.summarize(text, topic)
    health() 

    js = json.dumps({"summary": summary, "accuracy": accuracy, "text": str(text)})
    
    result = "Tracing requests"
    tracer.end_span()



    return jsonify(js)


if __name__ == "__main__":
   tracer = initialize_tracer()
   app.config['TRACER'] = tracer

   app.run(debug=True, host='0.0.0.0', port=5000)
