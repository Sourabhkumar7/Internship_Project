import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

input_df = pd.read_excel('input.xlsx')


def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.find('h1').get_text()
    
    paragraphs = soup.find_all('p')
    article_text = ' '.join([p.get_text() for p in paragraphs])
    
    return title + '\n' + article_text


if not os.path.exists('articles'):
    os.makedirs('articles')


for index, row in input_df.iterrows():
    url = row['URL']
    url_id = row['URL_ID']
    article_text = extract_text(url)
    
    with open(f'articles/{url_id}.txt', 'w', encoding='utf-8') as file:
        file.write(article_text)


