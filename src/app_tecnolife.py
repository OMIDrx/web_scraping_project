from bs4 import BeautifulSoup
import requests


url = 'https://www.technolife.com/category/mobile'
response = requests.get(url)


soup = BeautifulSoup(response.content,'html.parser')
print('-'*30)

description = soup.select('yekanbakh-en line-clamp-3  ')
print(len(description)) # number
for topic in description:
     print(topic.get_text())
    

price = soup.select('min-w-6 lg:min-w-7 flex  ')
print(len(price)) # number
for topic in price:
    print(topic.get_text())  
