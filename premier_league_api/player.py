"""Responsible for player stats"""
import warnings
from typing import Optional
from cached_property import cached_property
from .shared import Country


class PlayerStat:
    """Base stats for a player"""

    def __init__(self, data: dict):
        self._data = data

    @cached_property
    def name(self) -> str:
        """
        :return: Name of stat
        :rtype: str
        """
        return self._data["name"]

    @cached_property
    def value(self) -> int:
        """
        :return: Value of stat
        :rtype: int
        """
        return int(self._data["value"])

    @cached_property
    def description(self) -> str:
        """
        :return: Description of stat
        :rtype: str
        """
        return self._data["description"]

    @cached_property
    def additionalInfo(self) -> dict:
        """
        :return: Additional Info on stat. Usually empty
        :rtype: dict
        """
        return self._data["additionalInfo"]


class BasePlayer:
    """Base player"""

    def __init__(self, data: dict):
        self._data = data
        self.id = data["id"]

    def __str__(self) -> str:
        return self.fullName

    def __repr__(self) -> str:
        return self.fullName

    @cached_property
    def birthCountry(self) -> Country:
        """
        :return: Country born in
        :rtype: Country
        """
        return Country(self._data["birth"]["country"])

    @cached_property
    def nationalTeam(self) -> Country:
        """
        :return: Country played for
        :rtype: Country
        """
        return Country(self._data["nationalTeam"])

    @cached_property
    def birthday(self) -> str:
        """
        :return: Birthday of player
        :rtype: str
        """
        return self._data["birth"]["date"]["label"]

    @cached_property
    def birthtime(self) -> int:
        """
        :return: Epoch time representation of birthday
        :rtype: int
        """
        return int(self._data["birth"]["date"]["millis"])

    @cached_property
    def birthplace(self) -> Optional[str]:
        """
        :return: City of birth
        :rtype: str
        """
        try:
            return self._data["birth"]["place"]
        except KeyError:
            return None

    @cached_property
    def shirtNumber(self) -> int:
        """
        :return: Number worn by player
        :rtype: int
        """
        return self._data["info"]["shirtNum"]

    @cached_property
    def age(self) -> str:
        """
        :return: Age of player. Includes years and days
        :rtype: str
        """
        return self._data["age"]

    @cached_property
    def position(self) -> str:
        """
        :return: Position played. Either G, D, M, F
        :rtype: str
        """
        return self._data["info"]["position"]

    @cached_property
    def positionInfo(self) -> str:
        """
        :return: More detailed position
        :rtype: str
        """
        return self._data["info"]["positionInfo"]

    @cached_property
    def loan(self) -> bool:
        """
        :return: On loan
        :rtype: bool
        """
        return self._data["info"]["loan"]

    @cached_property
    def fullName(self) -> str:
        """
        :return: Player's full name
        :rtype: str
        """
        return self._data["name"]["display"]

    @cached_property
    def firstName(self) -> str:
        """
        :return: Player's first name
        :rtype: str
        """
        return self._data["name"]["first"]

    @cached_property
    def lastName(self) -> str:
        """
        :return: Player's last name
        :rtype: str
        """
        return self._data["name"]["last"]


class SearchPlayer(BasePlayer):
    """Search result for a player"""

    def __init__(self, data: dict):
        self._data = data
        super().__init__(data)

    @cached_property
    def height(self) -> int:
        """
        :return: Height in CM of the player
        :rtype: int
        """
        return self._data["height"]

    @cached_property
    def weight(self) -> int:
        """
        :return: Weight of player
        :rtype: int
        """
        return self._data["weight"]

    @cached_property
    def appearances(self) -> int:
        """
        :return: Amount of goals scored
        :rtype: int
        """
        return self._data.get("appearances")

    @cached_property
    def goals(self) -> int:
        """
        :return: Amount of goals
        :rtype: int
        """
        return self._data.get("goals")

    @cached_property
    def assists(self) -> int:
        """
        :return: Amount of assists
        :rtype: int
        """
        return self._data.get("assists")

    @cached_property
    def tackles(self) -> int:
        """
        :return: Amount of tackles
        :rtype: int
        """
        return self._data.get("tackles")

    @cached_property
    def shots(self) -> int:
        """
        :return: Amount of shots
        :rtype: int
        """
        return self._data.get("shots")

    @cached_property
    def keyPasses(self) -> int:
        """
        :return: Amount of key passes
        :rtype: int
        """
        return self._data.get("keyPasses")

    @cached_property
    def cleanSheets(self) -> int:
        """
        :return: Amount of clean sheets
        :rtype: int
        """
        return self._data.get("cleanSheets")

    @cached_property
    def saves(self) -> int:
        """
        :return: Amount of saves
        :rtype: int
        """
        return self._data.get("saves")

    @cached_property
    def goalsConceded(self) -> int:
        """
        :return: Amount of goals conceded
        :rtype: int
        """
        return self._data.get("goalsConceded")


class Player(BasePlayer):
    """Player object for full player"""

    def __init__(self, data: dict, generate_stats: bool = False):
        self._entity_data = data["entity"]
        super().__init__(data["entity"])
        self._stats_data = data["stats"]
        self._stats_generated = False
        if generate_stats:
            self.generate_stats()

    def generate_stats(self):
        """
        Generate the stats for the player.
        Not run by default because it adds around 150 attributes
        """
        if self._stats_generated:
            warnings.warn("Attempt to generate stats again")
            return
        self._stats_generated = True
        for x in self._stats_data:
            setattr(self, x["name"], PlayerStat(x))
