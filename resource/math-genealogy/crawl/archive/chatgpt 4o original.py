"""
chatgpt 4o spit out this code
for paring math genealogy website
"""
import requests
from bs4 import BeautifulSoup


def get_mathematician_data(mathematician_id):
    url = f"https://genealogy.math.ndsu.nodak.edu/id.php?id={283283}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Extracting the mathematician's name
        name = soup.find("h2").get_text()

        # Extracting advisor(s)
        advisors = []
        import re

        advisor_elements = soup.find_all(string=re.compile(r"Advisor \d:.*"))
        for advisor_element in advisor_elements:
            advisor_name = advisor_element.find_next_sibling("a").get_text()
            advisors.append(advisor_name)

        # Extracting students
        students = []
        # student_table = soup.find('table', {'class': 'studentstable'})
        student_table = soup.find_all("a", href=re.compile("id.php.*"))
        print("student_table", student_table)
        if student_table:
            student_links = student_table.find_all("a")
            for student_link in student_links:
                students.append(student_link.get_text())

        # Extracting dissertation title and school
        dissertation_info = soup.find("span", text="Dissertation:")
        if dissertation_info:
            dissertation_title = dissertation_info.find_next("br").next_sibling.strip()
        else:
            dissertation_title = "N/A"

        school_info = soup.find("span", text="School:")
        if school_info:
            school_name = school_info.find_next("br").next_sibling.strip()
        else:
            school_name = "N/A"

        # Return data as a dictionary
        data = {
            "name": name,
            "advisors": advisors,
            "students": students,
            "dissertation_title": dissertation_title,
            "school_name": school_name,
        }

        return data
    else:
        print(f"Error: Received status code {response.status_code}")
        return None


if __name__ == "__main__":
    mathematician_id = 18231  # Example ID, change to the desired mathematician's ID
    data = get_mathematician_data(mathematician_id)

    if data:
        print(f"Name: {data['name']}")
        print(f"Advisors: {', '.join(data['advisors'])}")
        print(f"Students: {', '.join(data['students'])}")
        print(f"Dissertation Title: {data['dissertation_title']}")
        print(f"School Name: {data['school_name']}")
