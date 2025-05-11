#importing libraries 
import requests
from bs4 import BeautifulSoup
import pandas as pd

#http Request to website
url = 'https://www.indeed.com/jobs?q=softare+engineer&l=New+York+city%2C+NY&from=searchOnHP&vjk=1d105def0857ac5e'
response = requests.get(url)

#parse content using beautiful soup 
soup = BeautifulSoup(response.text, 'html.parser')
