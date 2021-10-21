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

@app.route("/chart")
def chart():
    ufo_sightings = mongo.db.ufo_sightings.find_one()
    return render_template("index.html", ufo_sightings=ufo_sightings)
    # Filter the data
    df = pd.read_csv("shapes.csv")
    df = df[df['ID']>=5]
    #print(df)

    #Create the pie chart
    fig = px.pie(df, values='ID', names='Shape',
                title='Shapes of UFO Sightings',
                hover_data=['ID'], labels={'ID':'Total'})
    fig.update_traces(textposition='inside', textinfo='percent+label')
    #fig.show()
    return  html.Div([dcc.Graph(figure=fig)])

if __name__ == '__main__':
    app.run(debug=True)