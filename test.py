import pickle
import time

import requests
from selenium import webdriver


def get_cookies():
    url = 'https://www.baidu.com'
    web_driver = webdriver.Chrome()
    web_driver.get(url)

    username = web_driver.find_element_by_id('login-email')
    username.send_keys('username')
    password = web_driver.find_element_by_id('login-password')
    password.send_keys('password')
    login_button = web_driver.find_element_by_id('login-submit')
    login_button.click()
    time.sleep(3)
    cookies = web_driver.get_cookies()
    web_driver.close()
    return cookies


if __name__ == '__main__':
    cookies = get_cookies()
    pickle.dump(cookies, open('cookies.pkl', 'wb'))

#
# cookies = pickle.load(open('cookies.pkl', 'rb'))
# s = requests.Session()
# for cookie in cookies:
#     s.cookies.set(cookie['name'], cookie['value'])