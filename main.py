import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
# Top 200 = Web scrape
# Each uni = manual JSON file

# QMUL
"""
url = "https://www.qmul.ac.uk/undergraduate/coursefinder/courses/2023/electronic-engineering/"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# UNI + COURSE NAME
class Name:
    title = soup.find('title')
    print(title.string)

# BLANK
print()


# COURSE OVERVIEW
class CourseOverview:
    print('Course Overview')

    overview = soup.find('div', class_='tabs', id='structure-tabs')

    for ul_tag in overview.findAll('ul'):
        print(ul_tag.text)


# ENTRY REQUIREMENTS
class EntryRequirements:
    print("Entry Requirements")

    td_group = []
    tr_group = []

    e_r = soup.find('div', class_="disclosure-box__content prose")

    for td_tag in e_r.findAll('td', class_='fill'):
        td_group.append(td_tag.text)
        #print(td_tag.text)

    for tr_tag in e_r.findAll('tr'):
        tr_group.append(tr_tag.text)
        #print(tr_tag.text)

    for n in range(len(td_group)):
        print(td_group[n])
        print(tr_group[n])
"""
# TOP 200 SCRAPE

url = "https://en.wikipedia.org/wiki/List_of_top_1000_universities_in_the_world"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

data = []

# GET TABLE

table = soup.find('table', attrs={'class':'wikitable sortable'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

# print(*data, sep='\n')

# CLEAN TABLE (VALID RANKINGS ONLY) (Python)
clean_unis = []
<<<<<<< HEAD
top_150 = []
=======
top_200 = []
>>>>>>> 060377d33fdcd9f6c71ad2b3dba4e50eae83783c

for d in data:
    if len(d) > 2:
        if d[2].isdigit():
            clean_unis.append(d)

for c in clean_unis:
    if int(c[2]) < 200:
<<<<<<< HEAD
        top_150.append(c)
=======
        top_200.append(c)
>>>>>>> 060377d33fdcd9f6c71ad2b3dba4e50eae83783c

# print(*clean_unis, sep='\n')

# Pandas
<<<<<<< HEAD
df = pd.DataFrame(top_150)
=======
df = pd.DataFrame(top_200)
>>>>>>> 060377d33fdcd9f6c71ad2b3dba4e50eae83783c

# Pandas to HTML
print(df.to_html())
