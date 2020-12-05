from bs4 import BeautifulSoup
import requests
from word2number import w2n
import csv
import PyCurrency_Converter

url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
html_response = requests.get(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
soup = BeautifulSoup(html_response.text, 'lxml')

f = open('data.csv', 'w')
writer = csv.writer(f)
writer.writerow(['title', 'price', 'rating'])

for book in soup.findAll('article', class_='product_pod'):
    title = book.h3.a["title"]
    price_in_pounds = book.find('div', class_='product_price').find(
        'p', class_='price_color').text.replace('Â£', '')
    rating_in_words = book.find('p', class_='star-rating')['class'][1]
    rating = w2n.word_to_num(rating_in_words)
    writer.writerow([title, price, rating])
