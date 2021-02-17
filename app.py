from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import config


options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=options)
chrome.get("https://www.facebook.com/")

email = chrome.find_element_by_id("email")
password = chrome.find_element_by_id("pass")

email.send_keys('xxxxxx@gmail.com')
password.send_keys('xxxx')
password.submit()
time.sleep(3)
chrome.get('https://www.facebook.com/請填入fb帳號')

for x in range(1, 4):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)

soup = BeautifulSoup(chrome.page_source, 'html.parser')

titles = soup.find_all(
    'span', {'class': '請填入class'})

for title in titles:

    post = title.find('span', {'dir': 'auto'})

    if post:
        print(post.getText())

chrome.quit()
