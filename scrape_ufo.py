# Dependencies
from bs4 import BeautifulSoup as soup
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape_all():
    # Create path
    executable_path ={'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Define data
    data = {
        "ufo_sightings": ufo_sightings
        #"ufo_shapes": ufo_shapes,
        #"ufo_location": ufo_location
    }
    # Close browser
    browser.quit()
    return data

# Find all sightings
def ufo_sightings(browser):
    # Visit site
    url = "http://www.nuforc.org/webreports/ndxevent.html"
    browser.visit(url)

    html = broswer.html

    # Convert to soup object
    new_soup = soup(html, 'html.parser')

    # Make a list for ufo sightings
    ufo_sightings = []

    # Find all sightings
    links = browser.find_by_css("a.href")

    # Create loop
    for i in range(len(links)):
        sightings = {}
        browser.find_by_css("a.href")[i].click()
        try:
            ufo_sight = browser.links.find_by_text("City").first.first
            city = browser.find_by_css("td.font").text

            broswer.back()
        except:
            return None
    return ufo_sightings