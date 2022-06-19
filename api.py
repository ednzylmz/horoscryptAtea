from datetime import date
import json
from flask import Flask, request, jsonify, send_file
from flask_cors import cross_origin
from importlib_metadata import method_cache

from main import *

from azureadvanced import summarizer
app = Flask(__name__)

@app.route('/v1/api/vtt', methods=['GET'])
def get_vtt_transcript():
    return send_file('./artifacts/output.vtt', as_attachment=True, attachment_filename='output.vtt')

@app.route('/v1/api/start-analysis', methods=['POST'])
@cross_origin()
def start_analysis():
    content = request.json
    video = content['link']
    summary, dt, e = main(video)

    response = app.response_class(
        response=json.dumps({'s': summary, 'd': dt, 'e': e}),
        status=200,
        mimetype='application/json'
    )

    return response

@app.route('/v1/api/summary', methods=['GET'])
def get_vtt_summary():
    summary, _, _ = summarizer()
    print(summary)
    return summary

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from the url parameter /getmsg/?name=
    name = request.args.get("name", None)

    # For debugging
    print(f"Received: {name}")

    response = {}

    # Check if the user sent a name at all
    if not name:
        response["ERROR"] = "No name found. Please send a name."
    # Check if the user entered a number
    elif str(name).isdigit():
        response["ERROR"] = "The name can't be numeric. Please send a string."
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome API!"

    # Return the response in json format
    return jsonify(response)


@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome API!",
            # Add this option to distinct the POST request
            "METHOD": "POST"
        })
    else:
        return jsonify({
            "ERROR": "No name found. Please send a name."
        })


@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our teams transcript api!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=3001)