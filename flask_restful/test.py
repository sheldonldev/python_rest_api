import os
from dotenv import load_dotenv
import requests
from urllib.parse import urljoin
import random


load_dotenv()
BASE_URL = os.environ.get('BASE_URL')

# test
response = requests.get(urljoin(BASE_URL, 'helloworld'))
print(response.json())


data = [
    {"title": "spider", "views": 200000, "likes": 1000},
    {"title": "super man", "views": 300000, "likes": 3600},
    {"title": "arrows", "views": 400, "likes": 230},
]


for i in range(len(data)):
    response = requests.put(urljoin(BASE_URL, f'video/{str(i)}'), data[i])
    print(response.json())
    input()

response = requests.get(urljoin(BASE_URL, 'video/0'))
print(response.json())
input()

likes = random.randint(0, 300000)
response = requests.patch(urljoin(BASE_URL, 'video/0'), {'likes': likes})
print(response.json())
input()

response = requests.get(urljoin(BASE_URL, 'video/0'))
print(response.json())
input()

response = requests.delete(urljoin(BASE_URL, 'video/1'))
print(response.text)
input()

response = requests.get(urljoin(BASE_URL, 'video/1'))
print(response.json())
input()



