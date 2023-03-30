# Manhwa Web Scraper

This project is a web scraper that extracts information from a manhwa (Korean comics) website using the Python library BeautifulSoup.

## Installation

1.  Clone the repository to your local machine.
2.  Install the libraries: beautifulsoup4, html5lib, selenium.
3.  Run the scraper using `python scraper.py`.

## Usage

The scraper is designed to extract information from the manhwa website [https://1stkissmanga.me/](https://1stkissmanga.me/) without opening the browser. The script outputs the title and the link to the manhwa cover.

## How it works

The scraper works by using BeautifulSoup to parse the HTML of the manhwa website. It then searches for specific HTML tags and attributes to extract the desired information. The information will be stored in a Pandas dataframe and exported to a CSV file (yet to be implemented).
