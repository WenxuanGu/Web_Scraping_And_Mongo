#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from selenium import webdriver
import requests as req


# In[2]:


executable_path = {'executable_path' : 'chromedriver'}


# In[3]:


browser = Browser('chrome', **executable_path, headless = False)


# In[4]:


#scrape the NASA Mars News SIte, collect news title, paragraph text, assign
#to variables for later reference
url = "https://mars.nasa.gov/news/" 
response = req.get(url)

soup = bs(response.text, 'html5lib')

title = soup.find("div", class_="content_title").text
paragraph_text = soup.find("div", class_="rollover_description_inner").text


# In[5]:


#print(soup.prettify())


# In[6]:


print(paragraph_text)


# In[7]:


#Visit the URL for JPL's Space images
#splinter to navigate the site and find the image url for the current featured
#image and assign it to featured_image_url (use .jpg)
executable_path = {'executable_path' : 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)


# In[8]:


html = browser.html
soup = bs(html, "html.parser")


# In[9]:


browser.click_link_by_partial_text('FULL IMAGE')
#time.sleep(5)


# In[10]:


browser.click_link_by_partial_text('more info')


# In[11]:


new_html = browser.html
new_soup = bs(new_html, 'html.parser')
temp_img_url = new_soup.find('img', class_='main_image')
back_half_img_url = temp_img_url.get('src')

recent_mars_image_url = "https://www.jpl.nasa.gov" + back_half_img_url

print(recent_mars_image_url)


# In[12]:


#Get mars weather. SCRAPE THE DATA
browser.visit("https://twitter.com/marswxreport?lang=en")
time.sleep(5)
html = browser.html 
twitter_soup = bs(html, 'html.parser')


# In[13]:


print(twitter_soup)


# In[14]:


#print(soup.prettify())


# In[15]:


#twitter_url = "https://twitter.com/marswxreport?lang=en"


# In[16]:


#browser.visit(twitter_url)
#twitter_html = browser.html
#soup = bs(twitter_html, 'html.parser')


# In[17]:


tweet_containers = twitter_soup.find_all('div', attrs= { 'data-testid' : 'tweet' })


# In[18]:


print(tweet_containers)


# In[19]:


print(tweet_containers[0].text)


# In[20]:


p = tweet_containers[0].text


# In[21]:


tweet_containers[2].text 


# In[22]:


for tweets in tweet_containers:
    if tweets.text:
        print(tweets.text)
        break


# In[23]:


#Mars Facts....visit webpage, use pandas to scrape the page for facts, 
#convert pandas table to html table string. 
request_mars_space_facts = req.get("https://space-facts.com/mars/")


# In[24]:


mars_space_table_read = pd.read_html(request_mars_space_facts.text)


# In[25]:


#mars_space_table_read


# In[26]:


df = mars_space_table_read[0]
df


# In[27]:


df.set_index(0, inplace=True)


# In[28]:


mars_data_df = df
mars_data_df


# In[29]:


mars_data_html = mars_data_df.to_html()
mars_data_html


# In[30]:


mars_data_html.replace('\n', '')


# In[31]:


mars_data_df.to_html('mars_table.html')


# In[32]:


#..Visit the USGS Astrogeology site to obtain hgih resolution images for 
#....each of Mar's hemispheres
usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(usgs_url)
hemi_browser = browser.html 


# In[33]:


#..You will need to click each of the links to the hemispheres in order 
#....to find full res image
#soup = bs(hemi_browser, "html.parser")
hemi_attributes_list = browser.find_by_css("a.itemLink.product-item")


# In[34]:


print(hemi_attributes_list[3])


# In[35]:


browser.find_by_css("img.thumb")[0].click()


# In[44]:


html = browser.html


# In[45]:


soup = bs(html, "html.parser")
hemi_pic = soup.find('img', class_="wide-image") 


# In[47]:


print(hemi_pic['src'])


# In[51]:


for i in range(4):
    browser.find_by_css("img.thumb")[i].click()
    html = browser.html
    soup = bs(html, "html.parser")
    hemi_pic = soup.find('img', class_="wide-image") 
    print(hemi_pic['src'])
    browser.back()


# In[40]:


print(soup)


# In[ ]:


#href = "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"


# In[ ]:





# In[ ]:




