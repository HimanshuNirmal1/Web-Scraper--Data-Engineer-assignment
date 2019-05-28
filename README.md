# Web-Scraper--Data-Engineer-assignment
A python web scraper program 


Data Engineer Assignment- Web Scraping

Technologies used: Python 3.7
Libraries used: BeautifulSoup, requests and csv
Environments used: Anaconda-Spyder

Before scraping, see permission from the website that you are going to scrape from. At the end of the website’s main page, add ‘robot.txt’ to see permissions.
robots.txt is a standard used by websites to communicate with web crawlers and other web robots. The standard specifies how to inform the web robot about which areas of the website should not be processed or scanned.

If you do not have BeautifulSoup and requests, simply download them by typing following command in your command prompt:
Anaconda prompt: conda install -c anaconda beautifulsoup4
Anaconda prompt: conda install requests

Windows prompt: pip install beautifulsoup4, pip install requests

How to run: Run it like any other python program. 
python webscrape1.py

Description: In this assignment, we have scraped the Wikipedia page of top most populous US Cities. We have written the scraped content data into a UTF-8 Csv file which is ready to be uploaded on the BigQuery table.

Additionally, we also have scraped data from the second table of the page, and gathered the links of all cities and states, and displayed the scraped content data found on the webpages of first four links and wrote it in the csv file.

