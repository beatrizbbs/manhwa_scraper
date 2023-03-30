from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless')
options.add_argument('--headless=new')

dr = webdriver.Chrome(options=options)

dr.get("https://1stkissmanga.me/manga/i-dont-want-the-obssession-of-a-twisted-archduke/")

soup = BeautifulSoup(dr.page_source, "html5lib")

title = soup.find("div", class_="post-title")
image= soup.find("div", class_="summary_image").find("img").get('src')

print("Title: ", title.text.strip())
print("Image: ", image)

dr.quit()
