import requests
from bs4 import BeautifulSoup
import time
import csv


def get_soup(url):
    """Fetch the URL and return a BeautifulSoup object."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.text, "html.parser")


def extract_data(soup):
    """Extract relevant data from the BeautifulSoup object."""
    data = {}
    # Extract name
    data["Name"] = soup.title.string.split(" - ")[0] if soup.title else "Unknown"

    # Extract advisor information
    advisor_link = soup.find("p", style="text-align: center; line-height: 2.75ex").find("a")
    if advisor_link:
        data["Advisor"] = advisor_link.text.strip()
        data["Advisor_URL"] = advisor_link["href"]
    else:
        data["Advisor"] = "Unknown"
        data["Advisor_URL"] = None

    # Extract other details (this might need adjustment based on the site's structure)
    for tag in soup.find_all("p", style="text-align: center;"):
        if "Thesis" in tag.text:
            data["Thesis"] = tag.text.strip().split(": ", 1)[1]
        elif "Degree" in tag.text:
            data["Degree"] = tag.text.strip().split(": ", 1)[1]
        elif "University" in tag.text:
            data["University"] = tag.text.strip().split(": ", 1)[1]
        elif "Year" in tag.text:
            data["Year"] = tag.text.strip().split(": ", 1)[1]

    return data


def crawl_genealogy(start_url, max_depth=5, delay=1):
    """Crawl the genealogy tree up to a certain depth."""
    visited = set()
    queue = [start_url]
    all_data = []

    while queue and max_depth > 0:
        current_url = queue.pop(0)
        if current_url in visited:
            continue
        visited.add(current_url)

        soup = get_soup(current_url)
        data = extract_data(soup)
        all_data.append(data)

        if data["Advisor_URL"] and data["Advisor_URL"] not in visited:
            queue.append("https://genealogy.math.ndsu.nodak.edu/" + data["Advisor_URL"])
            time.sleep(delay)  # To avoid overloading the server

        max_depth -= 1

    return all_data


# Starting point, you might want to change this to your or someone else's ID
start_url = "https://genealogy.math.ndsu.nodak.edu/id.php?id=283283"  # Example ID

# Crawl the data
genealogy_data = crawl_genealogy(start_url)

# Write to CSV
with open("../math_genealogy.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = [
        "Name",
        "Advisor",
        "Advisor_URL",
        "Thesis",
        "Degree",
        "University",
        "Year",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in genealogy_data:
        writer.writerow(data)

print("Crawling completed. Data saved to 'math_genealogy.csv'.")
