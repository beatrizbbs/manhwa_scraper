from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re

def get_summary_item(item, soup):
    content = soup.find("h5", string=re.compile(r".*" + item + r".*")).parent.find_next_sibling("div", class_="summary-content")
    return content.text.strip()


options = Options()
options.add_argument("--headless")
options.add_argument("--headless=new")

dr = webdriver.Chrome(options=options)

dr.get("https://1stkissmanga.me/manga/i-dont-want-the-obssession-of-a-twisted-archduke/")

soup = BeautifulSoup(dr.page_source, "html5lib")

title = soup.find("div", class_="post-title")
image = soup.find("div", class_="summary_image").find("img").get("src")
summary = soup.find("div", class_="summary__content show-more")
alternative = get_summary_item('Alternative', soup)

print("Title: ", title.text.strip())
print("Image: ", image)
print("Summary: ", summary.text.strip())
print("Alternative titles: ", alternative)

dr.quit()
