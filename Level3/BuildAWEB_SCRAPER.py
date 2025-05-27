"""Develop a web scraper that extracts
specific data from websites using libraries
like BeautifulSoup or Scrapy. This task will
improve their knowledge of web scraping
techniques and handling HTML/XML data."""

import requests
from bs4 import BeautifulSoup
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Extract all headings (h1, h2, h3, etc.)
        headings = soup.find_all(['h1', 'h2', 'h3'])
        for heading in headings:
            print(heading.get_text(strip=True))
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        
def main():
    url = input("Enter the URL of the website to scrape: ")
    scrape_website(url)
if __name__ == "__main__":
    main()