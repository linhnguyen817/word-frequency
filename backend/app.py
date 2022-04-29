from urllib import request
# import flask
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from get_sorted_word_freq import getSortedWordFrequency

app = Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_SORT_KEYS'] = False    # maintains sortedness of dictionaries when using jsonify()

@app.route('/api/v1/get-sorted-word-frequency', methods=['GET'])
def apiGetWordFrequency():
    # Check if str was provided in request body
    # If no str is provided, return an error
    # try:
    #     str = request.get_json(force=True)
    #     # str = request.form.get('str')
    #     print("Input text: ", str)
    # except:
    #     return "Error: No string input provided."

    print("Input text: ", str)
    res = getSortedWordFrequency('my, name. is, chill-cdc. my nam!e is linh')
    print("Result: ", res)
    return jsonify(res)

app.run()
