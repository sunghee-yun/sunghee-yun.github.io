import requests
from bs4 import BeautifulSoup


def scrape_mathematician(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract data from the page (adjust selectors based on website structure)
    name = soup.find("h1").text
    advisor = soup.find("a", text="Advisor").find_next("a").text
    students = [a.text for a in soup.find_all("a", text="Student")]
    # ... extract other relevant data

    return {"name": name, "advisor": advisor, "students": students}


def main():
    # Replace with the base URL of the mathematician you want to start with
    start_url = "https://genealogy.math.ndsu.nodak.edu/id.php?id=283283"  # Replace with actual ID

    mathematician_data = scrape_mathematician(start_url)
    # Process and store the data
    print(mathematician_data)


if __name__ == "__main__":
    main()
