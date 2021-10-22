from flask import Flask, render_template, jsonify, url_for
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

@app.route("/")
def index():

    # Insert Visual 1
    df = pd.read_csv("shapes.csv")
    df = df[df['ID']>=5]
    #print(df)

    #Create the pie chart
    fig = px.pie(df, values='ID', names='Shape',
                title='Shapes of UFO Sightings',
                hover_data=['ID'], labels={'ID':'Total'})
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig1JSON = json.dumps(fig, cls =plotly.utils.PlotlyJSONEncoder)

    #Create Visual 2
    # Create sunburst
    sun_df = pd.read_csv("ufo_sightings_locations.csv")
    #print(sun_df)
    counts = sun_df["State"].value_counts()
    sun = px.sunburst(sun_df, title='Sunburst Plot of Locations', path=["State","City"], hover_name="City", color="City", height=700)
    #sun.show()
    fig2JSON = json.dumps(sun, cls =plotly.utils.PlotlyJSONEncoder)

    
    #Create Visual 3
    # Create a scatter plot
    # state_df = pd.read_csv("ufo_sightings_locations.csv")
    # state_df = state_df.groupby("State")["ID"].nunique()
    # state_df.to_csv("states.csv")
    #print(state_df)
    state_df=pd.read_csv("states.csv")
    scatter = px.scatter(state_df, x="State", y="ID", title="Scatter Plot by State Totals", height=900)
    #scatter.show()
    fig3JSON = json.dumps(scatter, cls =plotly.utils.PlotlyJSONEncoder)

    return render_template("index.html", fig1JSON = fig1JSON, fig2JSON = fig2JSON, fig3JSON = fig3JSON)

if __name__ == "__main__":
    app.run(debug=True)