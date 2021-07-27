"""Responsible for handing full gameweeks"""
from typing import Optional, List
from cached_property import cached_property
from .fixture import FixtureResult
from .shared import MatchTime


class GameWeeks:
    """Gameweeks represent a week of matches"""

    def __init__(self, data: dict):
        self._data = data

    def __str__(self) -> str:
        return f"Gameweek {self.gameweek_num} id: {self.id}"

    def __repr__(self) -> str:
        return f"Gameweek {self.gameweek_num} id: {self.id}"

    @cached_property
    def gameweek_num(self) -> int:
        """
        :return: Number of the gameweek
        :rtype: int
        """
        return self._data["gameweek"]

    @cached_property
    def start(self) -> MatchTime:
        """
        :return: Start of gameweek
        :rtype: MatchTime
        """
        return MatchTime(self._data["from"])

    @cached_property
    def end(self) -> MatchTime:
        """
        :return: End of gameweek
        :rtype: MatchTime
        """
        return MatchTime(self._data["until"])

    @cached_property
    def matches(self) -> int:
        """
        :return: Amount of matches in gameweek
        :rtype: int
        """
        return self._data["matches"]

    @cached_property
    def status(self) -> str:
        """
        :return: Status of the gameweek
        :rtype: str
        """
        return self._data["status"]

    @cached_property
    def id(self) -> int:
        """
        :return: ID of gameweek
        :rtype: int
        """
        return self._data["id"]


class GameWeekFixture(FixtureResult):
    """Gameweek fixture. Does not have fixture events"""

    def __init__(self, data: dict):
        super().__init__({"fixture": data})
        self.id = int(data["id"])

    @cached_property
    def goals(self) -> List["GameWeekGoal"]:
        """
        Goals scored in the fixture
        :return: List of goals
        :rtype: List[GameWeekGoal]
        """
        return [GameWeekGoal(x) for x in self._fixture_data["goals"]]


class GameWeekGoal:
    """Goal from a gameweek fixture"""

    def __init__(self, data: dict):
        self._data = data

    @cached_property
    def scorer(self) -> int:
        """
        :return: Id of player who scored the goal
        :rtype: int
        """
        return int(self._data["personId"])

    @cached_property
    def assist(self) -> Optional[int]:
        """
        :return: Id of player who assisted the score if any
        :rtype: int
        """
        try:
            return int(self._data.get("assistId"))
        except TypeError:
            return None

    @cached_property
    def seconds(self) -> int:
        """
        :return: Second when goal was scored
        :rtype: int
        """
        return self._data["clock"]["secs"]

    @cached_property
    def time(self) -> str:
        """
        :return: Time when goal was scored
        :rtype: str
        """
        return self._data["clock"]["label"]

    @cached_property
    def phase(self) -> int:
        """
        :return: Phase of the game when the goal was scored
        :rtype: str
        """
        return int(self._data["phase"])

    @cached_property
    def type(self) -> str:
        """
        :return: Type of goal. Either G for goal or P for penalty
        :rtype: str
        """
        return self._data["type"]

    @cached_property
    def description(self) -> str:
        """
        :return: Usually same as type
        :rtype: str
        """
        return self._data["description"]
