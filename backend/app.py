from urllib import request
from flask import Flask, request, jsonify
from flask_cors import CORS
from get_sorted_word_freq import getSortedWordFrequency

app = Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_SORT_KEYS'] = False    # maintains sortedness of dictionaries when using jsonify()

@app.route('/api/v1/get-sorted-word-frequency', methods=['POST'])
def apiCalculateWordFrequency():
    # Check if str was provided in request body
    # If no str is provided, return an error
    try:
        str = request.json['str']
        print("Input text: ", str)
    except:
        return "Error: No valid string input provided."

    print("Input text: ", str)
    res = getSortedWordFrequency(str)
    print("Result: ", res)
    return jsonify(res)

app.run()
