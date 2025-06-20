from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def scrapeArticle(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Initialize Selenium
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(4)  # Allow time for JavaScript to load

        # Get the full rendered page source
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        article_container = soup.find("div", class_="article__body")
        if not article_container:
            # Try fallback search using multiple <p> tags in the content section
            paragraphs = soup.find_all("p")
        else:
            paragraphs = article_container.find_all("p")

        # Join paragraph text
        article_text = "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))

        return article_text if article_text else "No readable content found."

    except Exception as e:
        return f"Scraping failed: {e}"

    finally:
        driver.quit()
