from flask import Flask, request, jsonify, render_template
from sum import model
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/summarize', methods=['POST'])
def predict():
    text = request.get_data()
    topic = request.args.get('topic')

    if not topic:
        return jsonify({"error": "no topic present"}), 400
    if not text.strip():
        return jsonify({"error": "empty text"}), 400

    summary, accuracy = model.summarize(text, topic)

    js = json.dumps({"summary": summary, "accuracy": accuracy, "text": str(text)})

    return jsonify(js)


if __name__ == "__main__":
    app.run(debug=True)
