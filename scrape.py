from bs4 import BeautifulSoup
import requests
import csv

soup = BeautifulSoup(requests.get("http://localhost:3000/").text, "lxml")

article = soup.find('div', class_='post')

# # 1. Title
# title = article.h3.text
# print(title)

# # 2. Summary
# summary = article.p.text
# print(summary)

# # 3. Link
# link = article.h3.a['href']
# print(link)

csv_file = open('data.csv', 'w', newline='')
writer = csv.writer(csv_file)

writer.writerow(['title', 'summary', 'link'])

articles = soup.find_all('div', class_='post')

for article in articles:
    title = article.h3.a.text
    summary = article.p.text
    link = "http://localhost:3000{0}".format(article.h3.a['href'])

    row = [title, summary, link]
    writer.writerow(row)

csv_file.close()
