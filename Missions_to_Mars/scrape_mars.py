from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from sre_constants import SUCCESS

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_dict = {}

    #Mars News
    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    mars_dict["news_title"] = soup.find_all('div', class_ = 'content_title')[0].text
    mars_dict["news_p"] = soup.find_all('div', class_ = 'article_teaser_body')[0].text

    print("SUCCESS1")
    
    #Mars Featured Image
    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    relative_image_path = soup.find_all('img')[1]["src"]
    mars_dict["featured_image_url"] = url + relative_image_path

    print("SUCCESS2")

    #Mars Facts Table

    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)

    tables_df = tables[1]

    cols = list(tables_df.columns)
    cols[0] = "Measurements"
    cols[1] = "Figures"

    tables_df.columns = cols

    html_table = tables_df.to_html()
    mars_dict["Mars_facts"] = html_table

    #Mars Hemispheres

    hemisphere_image_urls = []

    #Cerberus Hemisphere

    url = "https://marshemispheres.com/cerberus.html"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    cerberus_title = soup.find('h2', class_='title').text
    cerberus_image_path = soup.find_all('img')[4]["src"]
    cerberus_img = "https://marshemispheres.com/" + cerberus_image_path

    cerberus_dict = {'title': cerberus_title,'img_url': cerberus_img}

    hemisphere_image_urls.append(cerberus_dict)

    #Schiaparelli Hemisphere

    url = "https://marshemispheres.com/schiaparelli.html"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    schiaparelli_title = soup.find('h2', class_ = 'title').text
    schiaparelli_image_path = soup.find_all('img')[4]["src"]
    schiaparelli_img = "https://marshemispheres.com/" + schiaparelli_image_path

    schiaparelli_dict = {
        'title': schiaparelli_title,
        'img_url': schiaparelli_img
    }

    hemisphere_image_urls.append(schiaparelli_dict)

    #Syrtis Hemisphere

    url = "https://marshemispheres.com/syrtis.html"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    syrtis_title = soup.find('h2', class_ = 'title').text
    syrtis_major_image_path = soup.find_all('img')[4]["src"]
    syrtis_major_img = "https://marshemispheres.com/" + syrtis_major_image_path

    syrtis_dict = {
        'title': syrtis_title,
        'img_url': syrtis_major_img
    }

    hemisphere_image_urls.append(syrtis_dict)

    #Valles Hemisphere

    url = "https://marshemispheres.com/valles.html"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    valles_title = soup.find('h2', class_='title').text
    valles_image_path = soup.find_all('img')[4]["src"]
    valles_img = "https://marshemispheres.com/" + valles_image_path

    valles_dict = {
        'title': valles_title,
        'img_url': valles_img
    }

    hemisphere_image_urls.append(valles_dict)

    mars_dict["hemispheres"] = hemisphere_image_urls

    browser.quit()
    
    print (mars_dict)
    return mars_dict
