"""Shared classes"""
from typing import Optional
from cached_property import cached_property


class Team:
    """
    Class that represents a team
    """

    def __init__(self, data: dict):
        self.name = data["team"]["name"]
        self._data = data

    @cached_property
    def short_name(self) -> str:
        """
        :return: Short name of the team
        :rtype: str
        """
        return self._data["team"]["shortName"]

    @cached_property
    def id(self) -> int:
        """
        :return: ID of the team
        :rtype: int
        """
        return int(self._data["team"]["id"])

    @cached_property
    def team_type(self) -> str:
        """
        If the team is senior, U21, or U18

        :return: Type of team
        :rtype: str
        """
        return self._data["team"]["teamType"]

    @cached_property
    def score(self) -> Optional[int]:
        """
        :return: Number of goals scored
        :rtype: int
        """
        try:
            return int(self._data["score"])
        except KeyError:
            return None

    @cached_property
    def abbreviation(self) -> str:
        """
        :return: Abbreviation of the team
        :rtype: str
        """
        return self._data["team"]["club"]["abbr"]


class Country:
    """
    Class that presents a country
    """

    def __init__(self, data: dict):
        self._data = data

    @cached_property
    def iso_code(self) -> str:
        """
        :return: ISO code
        :rtype: str
        """
        return self._data["isoCode"]

    @cached_property
    def country(self) -> str:
        """
        :return: Name of country
        :rtype: str
        """
        return self._data["country"]

    @cached_property
    def demonym(self) -> str:
        """
        :return: Demonym of country
        :rtype: str
        """
        return self._data["demonym"]


class MatchTime:
    """Time of a match. Used for start and end"""

    def __init__(self, data: dict):
        self._data = data

    @cached_property
    def completeness(self) -> int:
        """
        :return: Completeness of the match.
            Uncertain as to the full range of values and what they mean
        :rtype: int
        """
        return self._data["completeness"]

    @cached_property
    def label(self) -> str:
        """
        :return: Label of time
        :rtype: str
        """
        return self._data["label"]

    @cached_property
    def epoch(self) -> int:
        """
        :return: Epoch time in milliseconds
        :rtype: int
        """
        return self._data["millis"]

    @cached_property
    def gmtOffset(self) -> int:
        """
        :return: GMT offset of time
        :rtype: int
        """
        return int(self._data["gmtOffset"])
