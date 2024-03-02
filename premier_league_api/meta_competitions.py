"""Generate competitions file"""

import os
import sys
from typing import List
import warnings
from datetime import datetime
import requests

FILE_HEADER = f"""\"\"\"DO NOT MANUALLY EDIT. FILE AUTOMATICALLY GENERATED BY meta_competitions.py
GENERATED AT: {datetime.now()} \"\"\"
# pylint: disable=too-few-public-methods,too-many-lines
from typing import Optional

"""
COMPETITION_TEXT = """
class {abbreviation}:
    \"\"\" Class for {description} \"\"\"
    description = "{description}"
    id = {id}
    level = "{level}"
    source = "{source}"
    abbreviation = "{abbreviation}"
    seasons = {seasons}

    @staticmethod
    def get_season_by_label(label: str) -> Optional[int]:
        \"\"\"
        Get a season by the label
        :param label: String of label
        :type label: str
        :return: Season ID
        :rtype: int
        \"\"\"
        return {abbreviation}.seasons.get(label)
"""


def download_competitions() -> List[str]:
    """
    Downloads and returns a list of filled out COMPETITION Text

    :return: List of filled out text
    :rtype: List[COMPETITION_TEXT]
    """
    competitions: list[dict] = []
    results = requests.get(
        "https://footballapi.pulselive.com/football/competitions",
        headers={"Origin": "https://www.premierleague.com"},
        params={"page": 0, "pageSize": 100, "detail": 2},
        timeout=10,
    )
    competitions.extend(results.json()["content"])
    next_page = results.json()["pageInfo"]["page"] + 1
    num_pages = results.json()["pageInfo"]["numPages"]
    while next_page <= num_pages:
        results = requests.get(
            "https://footballapi.pulselive.com/football/competitions",
            headers={"Origin": "https://www.premierleague.com"},
            params={"page": next_page, "pageSize": 100, "detail": 2},
            timeout=10,
        )
        results.raise_for_status()
        competitions.extend(results.json()["content"])
        next_page = results.json()["pageInfo"]["page"] + 1
    return [
        COMPETITION_TEXT.format(
            abbreviation=comp["abbreviation"].replace(" ", "_").replace("-", "_"),
            seasons={x["label"]: int(x["id"]) for x in comp["compSeasons"]},
            level=comp["level"],
            id=int(comp["id"]),
            description=comp["description"],
            source=comp.get("source"),
        )
        for comp in competitions
        if len(competitions) > 0
        and comp["abbreviation"][0].isdigit() is False
        and len(comp["compSeasons"]) > 0
    ]


def create_competitions_file():
    """
    Create a new competitions file
    """
    created_classes = download_competitions()
    with open(
        os.path.join(
            os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))),
            "competitions.py",
        ),
        "w",
        encoding="utf-8",
    ) as outfile:
        outfile.write(FILE_HEADER)
        for x in created_classes:
            outfile.write(f"{x}\n")


if __name__ == "__main__":
    create_competitions_file()
