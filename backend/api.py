from urllib import request
import flask
from flask import request, jsonify
from get_sorted_word_freq import getSortedWordFrequency

testInput = 'my, name. is, chill-cdc. my name is linh'

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_SORT_KEYS'] = False    # maintains sortedness of dictionaries when using jsonify()

@app.route('/api/v1/get-sorted-word-frequency', methods=['GET'])
def apiGetWordFrequency():
    # Check if str was provided in request body
    # If no str is provided, return an error
    try:
        str = request.json['str']
    except:
        return "Error: No string input provided."

    res = getSortedWordFrequency(str)
    print(res)
    return jsonify(res)

app.run()