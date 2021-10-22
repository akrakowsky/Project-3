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
  - Cleaning the data. The data frame was cleaned in the Jupyter Notebook first by creating a new column called locations and combing the city and state. All sightings without a reported city and state were dropped. The csv file us_cities.csv from https://github.com/kelvins/US-Cities-Database/blob/main/csv/us_cities.csv was merged to the data frame to add latitude and longitude to each location. This provided over 100,000 reports and was saved as a csv. To help with the flask app this data was also uploaded to MongoDB Compass
  - gsfgg
  - gsfgdsfs
  - sgsfsg

-----------
## Trouble-shooting

-----------
## Considerations

-----------

## Resources:
1. UFO Sightings Website: http://www.nuforc.org/webreports.html
2. List of lat and lng locations: https://github.com/kelvins/US-Cities-Database/blob/main/csv/us_cities.csv
3. Code with Prince-how to add plotly express visuals to flask app: https://www.youtube.com/watch?v=B97qWOUvlnU
