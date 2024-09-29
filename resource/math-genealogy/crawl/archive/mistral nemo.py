import requests
from bs4 import BeautifulSoup
import pandas as pd


# Function to extract mathematician data from a single page
def extract_data(url):
    response = requests.get(url)
    print("response", response)
    soup = BeautifulSoup(response.text, "html.parser")
    print("soup", soup)

    data = []
    for item in soup.select(".item"):
        print("XXX", item)
        name = item.select_one(".name").text.strip()
        birth_year = item.select_one(".birth").text.strip()
        death_year = item.select_one(".death").text.strip()

        data.append({"Name": name, "Birth Year": birth_year, "Death Year": death_year})

    return pd.DataFrame(data)


# Main function to crawl the website and extract data
def crawl_website():
    base_url = "https://genealogy.math.ndsu.nodak.edu/?id=283283"
    all_data = pd.DataFrame()

    for page in range(1, 10):  # The website has 100 pages
        url = f"{base_url}{page}"
        print(f"Crawling {url}...")
        data = extract_data(url)
        print(data)
        all_data = pd.concat([all_data, data], ignore_index=True)

    return all_data


# Crawl the website and save the data to a CSV file
if __name__ == "__main__":
    data = crawl_website()
    print(data)
    data.to_csv("mathematicians_data.csv", index=False)
    print("Data saved to 'mathematicians_data.csv'")
