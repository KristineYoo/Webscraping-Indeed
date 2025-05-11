#importing libraries 
import requests
from bs4 import BeautifulSoup
import pandas as pd

#http Request to website
url = 'https://www.indeed.com/jobs?q=softare+engineer&l=New+York+city%2C+NY&from=searchOnHP&vjk=1d105def0857ac5e'
response = requests.get(url)

#parse content using beautiful soup 
soup = BeautifulSoup(response.text, 'html.parser')

#extracing the data 
job_titles = soup.find_all('a', class_='jobtitle')
companies = soup.find_all('span', class_='company')
locations = soup.find_all('div', class_='location')
summaries = soup.find_all('div', class_='summary')

# Print the first job title, company, location, and summary
print(job_titles[0].text)
print(companies[0].text)
print(locations[0].text)
print(summaries[0].text)
