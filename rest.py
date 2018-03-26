#!flask/bin/python
from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/finData')
def get_fin_data():
    data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
    print 'DATA:', repr(data)

    data_string = json.dumps(data, indent=4, sort_keys=True)
    print 'JSON:', data_string
    return data_string

if __name__ == '__main__':
    app.run(debug=True)