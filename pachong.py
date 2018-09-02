# coding:utf-8

from urllib import request
import requests
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall


def main():
    page = requests.get('http://github.com/login')
    if page.status_code != 200:
        return
    cookies = page.cookies.get_dict()
    soup = BeautifulSoup(page.text, 'lxml')
    utf8_value = soup.select_one('form input[name=utf8]').attrs['value']
    authenticity_token_value = \
        soup.select_one('form input[name=authenticity_token]').attrs['value']
    data = {
        'utf8': utf8_value,
        'authenticity_token': authenticity_token_value,
        'login': 'xiongze',
        'password': 'xz1028877892'
    }

    page = requests.post('https://github.com/session',
                         data=data, cookies=cookies)
    print(page.text)


    # 获取页面内容
    page = request.urlopen('http://movie.douban.com/top250?format=text')
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


if __name__ == '__main__':
    main()

