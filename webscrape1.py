# -*- coding: utf-8 -*-
"""
Created on Fri May 24 19:24:57 2019

@author: Superman
"""



# Here, we're just importing both Beautiful Soup and the Requests library
from bs4 import BeautifulSoup
import requests
import csv



# this is the url that we've already determined is safe and legal to scrape from.
page_link = 'https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population'

# here, we fetch the content from the url, using the requests library
page_response = requests.get(page_link, timeout=5)

#we use the html parser to parse the url content and store it in a variable.
page_content = BeautifulSoup(page_response.content, "html.parser")



# looping through the paragraph element from the page and storing into the empty array
textContent = []
for i in range(0, 50):
    paragraphs = page_content.find_all("p")[i].text
    textContent.append(paragraphs)


#converting list into string
textContent = ''.join(textContent)
#print(type(textContent))
#print(textContent)

#splitting  
textContent=(textContent.split('\n '))
#print(textContent[1])


#writing all contents of textContent into a csv file 'webData' 
#encoding with utf-8 which is standard csv format for uploading to BigQuery table
for i in range(len(textContent)):
    mycsv = csv.writer(open('webData.csv', 'w',encoding='utf-8'))
    mycsv.writerow(textContent)
 
    

#parsed_table_data = []    
 
# in the section below we get the contents inside the i element from the table
   
links = []
additional_table = page_content.find('table',class_="sortable")
additional_table_td = additional_table.find_all('i');


# below we get the href links inside the <a> </a> tag

for link in additional_table.find_all('a'):
    
    name = link.find('title')
    
    if 'href' in link.attrs:
        #print(link.attrs['href'])
        if "/wiki/" in link.attrs['href']:
            links.append('https://en.wikipedia.org'+link.attrs['href'])


#writing all the links from the table ie from City and State column
mycsv.writerow(["All the links from City and State columns: "])
mycsv.writerow(links)  

#print(name) 
#print(url)


#Below we go inside the individual first 4 links/ pages from the additional table 
#ie New York City and Los Angeles from City column,
#and New York State and California from State column  
#displaying their initial content  from paragraph element

mycsv.writerow(['Going inside the individual pages of New York City, New York state, Los Angeles and California pages and displaying initial paragraph content: '])
for i in range(0,4):
    linkData = links[i];
    page_response = requests.get(linkData, timeout=5)
    # here, we fetch the content from the url, using the requests library
    page_content = BeautifulSoup(page_response.content, "html.parser")
    #we use the html parser to parse the url content and store it in a variable.
    insideLinkContent = []

    for i in range(0, 20):
        paragraphs1 = page_content.find_all("p")[i].text
        insideLinkContent.append(paragraphs1)


    insideLinkContent = ''.join(insideLinkContent)
    insideLinkContent=(insideLinkContent.split('\n '))
    #print(insideLinkContent[1])


    mycsv.writerow(insideLinkContent)


 #mycsv.writerow(["End of CSV file: "])


#end of code
