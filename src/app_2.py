from bs4 import BeautifulSoup
import requests

# url = 'https://maktabkhooneh.org/learn/machine-learning/'
# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')

# print(soup)

# items = soup.find_all('section' , attrs= {'class': 'cooperates flex flex-col w-full'})
# # print(len(items))
# # print(items[0])

# uni_items = items[0].find_all('span', 
# attrs = {'class': 'w-full whitespace-nowrap overflow-hidden text-ellipsis text-lg md:text-base lg:text-lg font-semibold'})
# print(len(uni_items))

# for title in uni_items:
#     print(title.get_text())

# uni_list = soup.select('section.cooperates.flex span.w-full')
# print(len(uni_list))
# for title in uni_list:
#     print(title.get_text())

# print('*'*30)

# topic_list = soup.select('div.grid.grid a.border-solid.border-black-100')
# print(len(topic_list))
# for topic in topic_list:
#     print(topic.get_text())

import streamlit as st
url = 'https://www.technolife.com/category/mobile'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

descriptions = soup.select('section.relative.w-full h2')
prices = soup.select('section.relative.w-full p.font-semiBold.leading-5')
images = soup.select('section.relative.w-full img')

print(len(descriptions))
print(len(prices))
print(len(images))

count = 0
from urllib.parse import urljoin

from urllib.parse import urljoin
import requests

count = 0

for img in images:
    src = img.get('src')

    if src:
        full_url = urljoin('https://www.technolife.com/', src)
        print(full_url)

        r = requests.get(full_url)

        with open(f'./images/new_mobiles/img_{count}.png', 'wb') as output:
            output.write(r.content)

        count += 1

# cols = st.columns(3)

# for j in range(10):
#     for i in range(3):