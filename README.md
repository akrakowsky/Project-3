# Project-3

# Table of Contents

## A. Project 3 UFO Sightings
Use data visualizations to tell a story

1. static
    1. files
       1. us_cities.csv
    2. fonts
       1. font sheets from Code With Prince
    3. main.css
2. templates
    1. index.html
3. run.py
4. app.py
5. scrape_ufo.ipynb
6. ufo_sightings_locations.csv
7. ufo_sightings.json
8. shapes.csv
9. License
10. ReadMe

-----------
## Introduction

  Ever look up into the night sky and for moment spot an unusual shape? NUFORC has captured the reported sightings of UFOs on their site and organized them by event date, shape, state and posted date. This site was first introduced in class as part of our Pandas training to fix the provided data and format the duration column. During class there was an interest in the locations of sightings. This project is diving deeper into that data and creating interactive visualizations.

-----------
## Process

  - The csv file provided in class did not include recent sightings as the data ended in 2014. To gather all of the current and previous posts, the NUFORC site was scraped using Jupyter Notebook. Scrape_ufo.ipynb has the documentation for scraping the site. The data was pulled from the Event Date Section as this had all of the fields listed in the table. Data was seperated to individual links for each month of the year. An executable path was created and a loop started to finad all table data(td) and pull all of the data into a dataframe.
  - Cleaning the data. The data frame was cleaned in the Jupyter Notebook first by creating a new column called locations and combing the city and state. All sightings without a reported city and state were dropped. Also dropeed were Canadian locations as not all sightings were formatted the same. The csv file us_cities.csv from https://github.com/kelvins/US-Cities-Database/blob/main/csv/us_cities.csv was merged to the data frame to add latitude and longitude to each location. This provided over 100,000 reports and was saved as a csv. To help with the flask app this data was also uploaded to MongoDB Compass.
  - In MongoDb the data was converted to a JSON file.
  - Visual Studio Code was used to create the python and html files to create the flask app. 
     - app.py: Used to upload the information in MongoDB.
     - run.py: The flask app was initialized to create the 3 interactive visualizations by pulling the data. Plotly express was used to create the charts as it has a variety of options and added interction for the viewer. Chart 1: Pie chart that pulled each reported shape and the value. Chart 2: Sunburst plot of each state and the cities within each state. Chart 3: Scatter plot of each state with the value of reported sightings.
     - index.html: Bootstrap was used to format the page and create a container for the visuals. A brief statement about the charts were added as paragraphs. To keep the charts as interactive versus static, the figures were created as variables and added as script. 
     - main.css: is the styling sheet that formats the landing page. This sheet pulls in font styles provided by Code with Prince.

-----------
## Problems during the project

  - Figuring out how to pull the data took some time as the site stored each month of the year as a link to the table.
  - There was a lot of data being pulled and the first time running the notebook to pull each table took 40 minutes.
  - The initial plan was to use leaflet to create a heatmap and that's why the lat and long data was added. After creating the js file and trying to run the python file, the map worked and showed as expected. Came back the following days and ran the file again and the map was no longer displaying properly in multiple browsers. The decisiion was made to switch to plotly as it also provided more visuals.
  - At first plotting the charts from plotly express they were not interactive when the app was run. With research the youtube video by code with Prince explained how to correct that problem.
-----------
## Considerations

  - Starting with a smaller data set then trying the process and the full set would have been better. The large amount of data slowed down the perfomance at some points.
  - If revisited, it would be helpful in story-telling to have the heat map.

-----------

## Resources:
1. UFO Sightings Website: http://www.nuforc.org/webreports.html
2. List of lat and lng locations: https://github.com/kelvins/US-Cities-Database/blob/main/csv/us_cities.csv
3. Code with Prince-how to add plotly express visuals to flask app: https://www.youtube.com/watch?v=B97qWOUvlnU
