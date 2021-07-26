"""Gameweek Fixture Results"""
from typing import List, Optional
from cached_property import cached_property
from .shared import Team


class FixtureResult:
    """Results of fixture that has completed"""

    def __init__(self, data: dict):
        self._fixture_data = data["fixture"]
        self._raw_data = data
        self.id = data["fixture"]["id"]

    @cached_property
    def gameweek(self) -> int:
        """
        :return: Gameweek of fixture
        :rtype: int
        """
        return int(self._fixture_data["gameweek"]["gameweek"])

    @cached_property
    def events(self) -> Optional[List["FixtureEvent"]]:
        """
        :return: Events of the match. A gameweek fixture will return an empty list
        :rtype: List[FixtureEvent]
        """
        try:
            return [FixtureEvent(x) for x in self._raw_data["events"]["content"]]
        except KeyError:
            return []

    @cached_property
    def outcome(self) -> str:
        """
        :return: Outcome of match
        :rtype: str
        """
        return self._fixture_data["outcome"]

    @cached_property
    def neutral(self) -> bool:
        """
        :return: Fixture played a neutral ground
        :rtype: bool
        """
        return self._fixture_data["neutralGround"]

    @cached_property
    def attendance(self) -> int:
        """
        :return: Reported attendance
        :rtype: int
        """
        return int(self._fixture_data["attendance"])

    @cached_property
    def winner(self) -> Optional["Team"]:
        """
        :return: Winning team. None if draw
        :rtype: FixtureTeam
        """
        if self.outcome == "H":
            return self.homeTeam
        if self.outcome == "A":
            return self.awayTeam
        return None

    @cached_property
    def score(self) -> str:
        """
        :return: Score with full team names
        :rtype: str
        """
        return (
            f"{self.homeTeam.name}: {self.homeTeam.score} "
            f"- {self.awayTeam.name}: {self.awayTeam.score}"
        )

    @cached_property
    def short_score(self) -> str:
        """
        :return: Score with short team names
        :rtype: str
        """
        return (
            f"{self.homeTeam.short_name}: {self.homeTeam.score} "
            f"- {self.awayTeam.short_name}: {self.awayTeam.score}"
        )

    @cached_property
    def abbr_score(self) -> str:
        """
        :return: Score with team
        :rtype: str
        """
        return (
            f"{self.homeTeam.abbreviation}: {self.homeTeam.score} "
            f"- {self.awayTeam.abbreviation}: {self.awayTeam.score}"
        )

    @cached_property
    def homeTeam(self) -> "Team":
        """
        :return: Home team for the fixture
        :rtype: FixtureTeam
        """
        return Team(self._fixture_data["teams"][0])

    @cached_property
    def awayTeam(self) -> "Team":
        """
        :return: Away team for the fixture
        :rtype: FixtureTeam
        """
        return Team(self._fixture_data["teams"][1])

    @cached_property
    def city(self) -> str:
        """
        :return: City where the game was played
        :rtype: str
        """
        return self._fixture_data["ground"]["city"]

    @cached_property
    def stadium(self) -> str:
        """
        :return: Stadium where the game was played
        :rtype: str
        """
        return self._fixture_data["ground"]["name"]

    @cached_property
    def seconds(self) -> int:
        """
        :return: Total seconds of the match
        :rtype: int
        """
        return int(self._fixture_data["clock"]["secs"])

    @cached_property
    def time(self) -> str:
        """
        :return: Final clock time
        :rtype: str
        """
        return self._fixture_data["clock"]["label"]


class FixtureEvent:
    """
    Represents an event that happened in the fixture
    """

    def __init__(self, data: dict):
        self._data = data
        self.id = data["id"]
        self.type = data["type"]

    def __str__(self) -> str:
        return f"{self.description}"

    def __repr__(self) -> str:
        return f"{self.seconds}: {self.description}"

    @cached_property
    def description(self) -> str:
        """
        :return: Description of the event
        :rtype: str
        """
        return self._data["text"]

    @cached_property
    def players(self) -> List[int]:
        """
        :return: Players ids involved
        :rtype: List[int]
        """
        return self._data.get("playerIds")

    @cached_property
    def seconds(self) -> int:
        """
        :return: Second of the game when the event happened
        :rtype: int
        """
        return int(self._data["time"]["secs"]) if self._data.get("time") else None

    @cached_property
    def timeLabel(self) -> str:
        """
        :return: Clock time of the event
        :rtype: str
        """
        return self._data["time"]["label"] if self._data.get("time") else None
