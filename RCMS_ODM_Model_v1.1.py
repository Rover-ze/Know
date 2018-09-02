# coding:utf-8

from urllib import request
import re

import requests
from bs4 import BeautifulSoup
from distutils.filelist import findall

# 读
# 获取页面内容
url = 'http://movie.douban.com/top250?format=text'
page = request.urlopen(url)
contents = page.read()
print(contents)
soup = BeautifulSoup(contents, "html.parser")
print(soup)

# for tag in soup.find_all('div', class_='info'):
#     # print tag
#     m_name = tag.find('span', class_='title').get_text()
#     m_rating_score = float(tag.find('span', class_='rating_num').get_text())
#
#     print(m_name + "=" + str(m_rating_score))


# 存
data = {
    'name': 'nginx'
}
files = {'file': open("abc.csv", 'rb')}

response = requests.post(url, data=data, files=files)
