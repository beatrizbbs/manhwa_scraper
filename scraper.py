from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re

def get_summary_item(item, soup):
    content = soup.find("h5", string=re.compile(r".*" + item + r".*")).parent.find_next_sibling("div", class_="summary-content")
    return content.text.strip()

def extract_korean_title(text):
    hangul_regex = re.compile('[^ 가-힣]+')
    return hangul_regex.sub('', text).strip()

def get_genres(soup):
    genres = [genre.text.strip() for genre in \
              soup.find("div", class_="genres-content").findAll("a")]
    return ", ".join(genres)

def get_chapter_numbers(soup):
    return len(soup.findAll("li", class_="wp-manga-chapter"))


options = Options()
options.add_argument("--headless")
options.add_argument("--headless=new")

dr = webdriver.Chrome(options=options)

dr.get("https://1stkissmanga.me/manga/a-way-to-protect-the-lovable-you/")

soup = BeautifulSoup(dr.page_source, "html5lib")

title = soup.find("div", class_="post-title")
image = soup.find("div", class_="summary_image").find("img").get("src")
summary = soup.find("div", class_="summary__content show-more").text.strip()
korean_title = extract_korean_title(summary)
genres = get_genres(soup)
chapters_numbers = len(soup.findAll("li", class_="wp-manga-chapter"))

print("Title: ", title.text.strip())
print("Korean title: ", korean_title)
print("Genres: ", genres)
print("Chapters released: ", chapters_numbers, " chapters")
print("Image: ", image)
print("Summary: ", summary)

dr.quit()
