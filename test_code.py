from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=r'/snap/bin/chromium')
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
print("one")
browser = webdriver.Chrome(service=service, options=options)
print("two")
type(browser)
print("three")
browser.get('https://inventwithpython.com')
print("four")
# "/mnt/c/Program Files/Google/Chrome/Application"
