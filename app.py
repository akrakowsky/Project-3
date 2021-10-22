from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/ufo_db")

@app.route('/')
def db_ping():

    return render_template('index.html', data = 'UFO Sightings')
    

@app.route('/data')
def db_data():

    db_data = mongo.db.ufo_sightings.find({}, {'_id': False})
    print('this route was pinged')
    parsed = [x for x in db_data]
    # print('parsed: ', parsed)
    return jsonify(parsed)

if __name__ == '__main__':
    app.run(debug=True)