""" chatgpt 4o spit out this code
for paring math genealogy website
"""

from click import command, argument
import json
from logging import getLogger, Logger
import re
from typing import Any

import requests
from bs4 import BeautifulSoup

from freq_used.logging_utils import set_logging_basic_config

logger: Logger = getLogger()


class StopCrawlingException(Exception):
    pass


def refine_name_string(name: str) -> str:
    return re.sub(r"\s+", " ", name.strip())


def crawl(data: dict[str, Any], id_: str, depth_: int, height: int, /) -> None:

    if depth_ < 0 or id_ in data:
        return

    url = f"https://genealogy.math.ndsu.nodak.edu/id.php?id={id_}"
    response = requests.get(url)

    if response.status_code != 200:
        logger.warning(f"For id={id_}, request received status code {response.status_code}")
        return

    soup = BeautifulSoup(response.content, "html.parser")

    # Extracting the mathematician's name
    try:
        name: str = refine_name_string(soup.find("h2").get_text())
    except AttributeError:
        return

    # Extracting advisor(s)
    advisors = []
    advisor_elements = soup.find_all(string=re.compile(r"Advisor(\s+\d)?:.*"))
    for advisor_element in advisor_elements:
        try:
            advisor_name: str = refine_name_string(
                advisor_element.find_next_sibling("a").get_text()
            )
        except AttributeError as e:
            logger.warning(f"AttributeError: {e}, {advisor_element}")
            return

        advisor_id: str = re.match(  # type:ignore
            r"id\.php\?id=(\d+)$", advisor_element.next_element.attrs["href"]
        ).group(1)
        advisors.append(dict(name=advisor_name, id=advisor_id))

    data[id_] = dict(id=id_, name=name, advisors=advisors, height=height - depth_)
    logger.info(f"depth - {depth_}, id - {id_}, name - {name}")

    # if name.startswith("Carl Friedrich"):
    #     raise StopCrawlingException()

    for advisor in advisors:
        crawl(data, advisor["id"], depth_ - 1, height)


@command()
@argument("mathematician_id", type=str)
@argument("graph-depth", type=int)
def main(mathematician_id: str, graph_depth: int) -> None:
    set_logging_basic_config(__file__)

    my_id: str = mathematician_id
    my_math_gen_data: dict[str, dict[str, Any]] = dict()
    try:
        crawl(my_math_gen_data, my_id, graph_depth, graph_depth)
    except StopCrawlingException:
        pass

    logger.info(json.dumps(my_math_gen_data, indent=2))
    with open(f"my_math_gen - {graph_depth}.json", "w") as fid:
        json.dump(my_math_gen_data, fid, indent=2)


if __name__ == "__main__":
    main()
