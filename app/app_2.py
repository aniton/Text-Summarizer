from flask import Flask, request, jsonify, render_template
from parser import wikipedia
from summary import model
import json

app = Flask(__name__)



@app.route('/')
def home():
    return 'Wiki URL summarizer service. Please use /wikipedia '


@app.route('/health')
def health():
    return 'alive', 200


@app.route('/wikipedia', methods=['POST'])
def parse():
    title = request.args.get('title')
    topic = request.args.get('topic')

    text = wikipedia.wiki_parser(title)

    summary, accuracy = model.summarize(text, topic)

    js = json.dumps({"summary": summary, "accuracy": accuracy, "text": str(text)})

    return jsonify(js)


# @app.route('/wikipedia/url', methods=['POST'])
# def parse():
#     url = request.args.get('url')
#     topic = request.args.get('topic')
#
#     text = wikipedia.wiki_url(url)
#
#     summary, accuracy = model.summarize(text, topic)
#
#     js = json.dumps({"summary": summary, "accuracy": accuracy, "text": str(text)})
#
#     return jsonify(js)
#
#
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)