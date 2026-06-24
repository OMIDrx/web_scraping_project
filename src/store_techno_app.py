import streamlit as st
import requests
from bs4 import BeautifulSoup


url = 'https://www.technolife.com/category/mobile'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')


descriptions = soup.select('section.relative.w-full h2')
prices = soup.select('section.relative.w-full p.font-semiBold.leading-5')
images = soup.select('section.relative.w-full img')




count = 0
cols = st.columns(3)

for i in range(len(images)):

    src = images[i].get('src')
    full_url = 'https://www.technolife.com/' + src
    r = requests.get(full_url)
    if count == 3:
        count = 0
    with cols[count]:
        if count < 3:
            print(count)
            st.image(r.content)
            st.write(f'توضیحات: {descriptions[i].get_text()}')
            st.write(f'قیمت: {prices[i].get_text()}')
            count +=1
            
