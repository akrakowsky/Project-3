import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio
from flask import Flask
import dash_core_components as dcc
import dash_html_components as html

app = Flask(__name__)

 # Initialize PyMongo to work with MongoDBs
mongo = PyMongo(app, uri="mongodb://localhost:27017/ufo_db")

@app.route('/')
def index():
    ufo_sightings = mongo.db.ufo_sightings.find_one()
    return render_template("index.html", ufo_sightings=ufo_sightings)

@app.route("/chart")
def chart():
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

if __name__ == "__main__":
    app.run(debug=True)
# # Create sunburst
# sun_df = pd.read_csv("ufo_sightings_locations.csv")
# #print(sun_df)
# sun = px.sunburst(sun_df, path=["State","City"], hover_name="City", color="ID", height=700)
# sun.show()

# # Create a scatter plot
# # state_df = pd.read_csv("ufo_sightings_locations.csv")
# # state_df = state_df.groupby("State")["ID"].nunique()
# # state_df.to_csv("states.csv")
# #print(state_df)
# state_df=pd.read_csv("states.csv")
# scatter = px.scatter(state_df, x="State", y="ID", height=900)
# scatter.show()
