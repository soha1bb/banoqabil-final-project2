import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

def scrape_text_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    all_data = []

    for tag in soup.find_all(['p', 'li']):
        text_data = tag.get_text(strip=True)
        if not tag.find('img'):
            all_data.append([text_data])

    return all_data

def save_to_csv(data, filename='output_data.csv'):
    column_names = ['Data']
    df = pd.DataFrame(data, columns=column_names)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    url_to_scrape = input("Enter the URL to scrape: ")

    html_content = get_html(url_to_scrape)

    if html_content:
        scraped_data = scrape_text_data(html_content)
        if scraped_data:
            save_to_csv(scraped_data)

if __name__ == "__main__":
    main()
