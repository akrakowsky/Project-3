import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio

# Filter the data
df = pd.read_csv("shapes.csv")
df = df[df['ID']>=5]
#print(df)

#Create the pie chart
fig = px.pie(df, values='ID', names='Shape',
             title='Shapes of UFO Sightings',
             hover_data=['ID'], labels={'ID':'Total'})
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()

# Create sunburst
sun_df = pd.read_csv("ufo_sightings_locations.csv")
#print(sun_df)
sun = px.sunburst(sun_df, path=["State","City"], hover_name="City", color="ID", height=700)
sun.show()

# Create a scatter plot
# state_df = pd.read_csv("ufo_sightings_locations.csv")
# state_df = state_df.groupby("State")["ID"].nunique()
# state_df.to_csv("states.csv")
#print(state_df)
state_df=pd.read_csv("states.csv")
scatter = px.scatter(state_df, x="State", y="ID", height=900)
scatter.show()
