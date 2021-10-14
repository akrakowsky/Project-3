# import libraries
from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
import scrape_ufo

# Create app
app = Flask(__name__)

# Initializa PyMongo to work with MongoDB
mongo = PyMongo(app, uri="mongodb://localhost:27017/ufo_db")

# Create route
@app.route('/')
def index():
    ufos = mongo.db.ufos.find_one()
    return render_template('index.html', data = ufos)
    

@app.route('/scrape')
def scrape():
    ufos = mongo.db.ufos
    ufo_data = scrape_ufo.scrape_all()
    ufos.update({}, ufo_data, upsert=True)
    return redirect("/", code=302)

if __name__ == '__main__':
    app.run(debug=True)
