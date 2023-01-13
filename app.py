import json

from flask import Flask, jsonify
import boto3

app = Flask(__name__)

s3 = boto3.client('s3')


@app.route('/')
def index():
    return "Hello World! :)"


@app.route('/api/v1/data', methods=['GET'])
def get_data():
    """Method GET"""
    try:
        obj = s3.get_object(Bucket='mybucket', Key='data1.txt')
        data = obj['Body'].read()
        return data
    except:
        return "Error"


@app.route('/api/v1/add-data/<key>/<value>', methods=['PUT', 'GET'])
def put_data(key, value):
    """Method PUT"""
    data = json.dumps({key: value,})
    try:
        s3.put_object(Body=data, Bucket='mybucket', Key='data1.txt')
        return jsonify({'data': data}), 201
    except:
        return "Error"


if __name__ == '__main__':
    app.run(debug=True)
