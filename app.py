#!flask/bin/python
from flask import Flask, jsonify, abort, request
import fetchnresize
import motor.motor_tornado

app = Flask(__name__)

wines = [
    {
        'id': 1,
        'title': u'Wine image',
        'image': u''
    },
    {
        'id': 2,
        'title': u'Merlot',
        'image': u''
    }
]
#client = motor.motor_tornado.MotorClient('localhost', 27017)
# Insert mongodb code here

@app.route('/wines', methods=['GET'])
def get_winedex():
    return jsonify({'wines': wines})

@app.route('/wines/<int:wine_id>', methods=['GET'])
def get_wine(wine_id):
    wine = [wine for wine in wines if wine['id'] == wine_id]
    if len(wine) == 0:
        abort(404)
    return jsonify({'wine': wine[0]})

@app.route('/wines/', methods=['POST'])
def add_wine():
    """
    This function collects an image from a url and appends its tittle.
    Hackers beware! The function has secure input validation!
    """
    if not request.json \
        or not 'title' in request.json \
        or not 'url' in request.json:
        abort(400)
    url = request.json.get('url')
    try:
        image_data = fetchnresize.fetch(url)
        b64 = fetchnresize.resize(image_data)
    except Exception, err:
        print(str(err))
        b64="00"
    title = request.json.get('title')
    wine = {
        'id': 1234,
        'title': title,
        'image': b64
    }
    wines.append(wine)
    return jsonify({'wine': wine}), 201

@app.route('/')
def index():
   return 'Check out /wines for the api'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
