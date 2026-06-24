from bs4 import BeautifulSoup
import requests

url = 'https://maktabkhooneh.org/learn/machine-learning/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

 uni_items = items[0].find_all('span', 
 attrs = {'class': 'w-full whitespace-nowrap overflow-hidden text-ellipsis text-lg md:text-base lg:text-lg font-semibold'})
 print(len(uni_items))

 for title in uni_items:
     print(title.get_text())

 uni_list = soup.select('section.cooperates.flex span.w-full')
 print(len(uni_list))
 for title in uni_list:
    print(title.get_text())

print('*'*30)

topic_list = soup.select('div.grid.grid a.border-solid.border-black-100')
print(len(topic_list))
for topic in topic_list:
    print(topic.get_text())
