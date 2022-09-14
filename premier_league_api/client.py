"""API Client for requests"""
from typing import List
import requests
from .player import Player, SearchPlayer
from .gameweek import GameWeekFixture, GameWeeks
from .fixture import FixtureResult
from .shared import Team
from .errors import EmptyResponse

BASE_URL = "https://footballapi.pulselive.com/"
STANDARD_URL = f"{BASE_URL}football/"
AUTHED_HEADER = {"Origin": "https://www.premierleague.com"}


class APIClient:
    """
    Main api client that handles making all the requests and classes
    """

    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update(AUTHED_HEADER)

    def get_player(
        self,
        player_id: int,
        comp_id: int = None,
        season_id: int = None,
        generate_stats: bool = False,
    ) -> Player:
        """
        Get a player by their ID

        :param generate_stats: Generate the stats for the player. Defaults to false
        :type generate_stats: bool
        :param player_id: ID of the player
        :type player_id: int
        :param comp_id: Competition ID of the competition to get stats for
        :param season_id: Season ID to get stats for. You can use this without competition ID
        :return: The player
        :rtype: Player
        """
        return Player(
            self._get(
                url=f"{STANDARD_URL}/stats/player/{player_id}",
                params={"comps": comp_id, "compSeasons": season_id},
            ),
            generate_stats=generate_stats,
        )

    def search_player(
        self, player_name: str, league_name: str = "PremierLeague"
    ) -> List[SearchPlayer]:
        """
        Searches for a player by a name

        :param player_name: Full or partial name of the player
        :type player_name: str
        :param league_name:
        :type league_name: str
        :return: Possible matches. Max length of 30

        Todo:
        Implement pagination for results

        """
        return [
            SearchPlayer(x["response"])
            for x in self._get(
                url=f"{BASE_URL}search/{league_name}/",
                params={
                    "terms": player_name,
                    "type": "player",
                    "size": 30,
                    "start": 0,
                    "fullObjectResponse": True,
                },
            )["hits"]["hit"]
        ]

    def get_fixtures(
        self, season_id: int, gameweek: int = None
    ) -> List[GameWeekFixture]:
        """
        Get a list of all the fixtures in a season/gameweek

        :param season_id: Season ID to get fixtures for
        :type season_id: int
        :param gameweek: Gameweek to get fixtures for. If left out will return the entire season
        :return: List of GameWeekFixture
        :rtype: List[GameWeekFixture]
        """
        if gameweek is None:
            num_fixtures = self._get(
                url=f"{STANDARD_URL}fixtures",
                params={"compSeasons": season_id, "pageSize": 1},
            )
        return [
            GameWeekFixture(x)
            for x in self._get(
                url=f"{STANDARD_URL}fixtures",
                params={
                    "compSeasons": season_id,
                    "gameWeek": gameweek,
                    "sort": "asc",
                    "pageSize": num_fixtures["pageInfo"]["numEntries"]
                    if gameweek is None
                    else None,
                },
            )["content"]
        ]

    def get_fixture(self, fixture_id: int, language_code: str = "EN") -> FixtureResult:
        """
        Get a fixture by ID

        :param fixture_id: Id of the fixture to get
        :type fixture_id: int
        :param language_code: Language code to get.
            Note: Changing to anything but EN seems to leave the Fixture events blank
        :type language_code: str
        :return: Fixture
        :rtype: FixtureResult
        """
        return FixtureResult(
            self._get(
                url=f"{STANDARD_URL}fixtures/{fixture_id}/textstream/{language_code}",
                params={"pageSize": 500, "sort": "asc"},
            )
        )

    def get_teams_in_season(self, season_id: int) -> List[Team]:
        """
        Get all the teams that are taking part in a season

        :param season_id: Season ID to get
        :type season_id: int
        :return: List of teams for the season
        :rtype: List[Team]
        """
        return [
            Team({"team": x})
            for x in self._get(
                url=f"{STANDARD_URL}teams",
                params={
                    "pageSize": 100,
                    "compSeasons": season_id,
                    "altIds": True,
                    "page": 0,
                },
            )["content"]
        ]

    def get_gameweeks(self, season_id: int) -> List[GameWeeks]:
        """
        Get gameweeks for a season

        :param season_id: Id of the season
        :type season_id: int
        :return: Gameweeks in the season
        :rtype: List[GameWeeks]
        """
        return [
            GameWeeks(x)
            for x in self._get(url=f"{STANDARD_URL}compseasons/{season_id}/gameweeks")[
                "gameweeks"
            ]
        ]

    def get_gameweek(
        self, season_id: int, gameweek: int, matches_per_week: int = 10
    ) -> List[GameWeekFixture]:
        """
        Get fixtures for a specific gameweek of the season

        :param season_id: Season ID of the season that the gameweek took place in
        :type season_id: str

        :param gameweek: Number of the game week to get
        :type gameweek: int

        :param matches_per_week: How many matches there are per game week.
            It should be equal to half the amount of teams. Elimination tournaments will be tricky
        :type matches_per_week: int

        :return: List of matches
        :rtype: List[GameWeekFixture]
        """
        return [
            GameWeekFixture(x)
            for x in self._get(
                url=f"{STANDARD_URL}fixtures",
                params={
                    "compSeasons": season_id,
                    "page": gameweek - 1,
                    "pageSize": matches_per_week,
                    "sort": "asc",
                    "statuses": "C",
                },
            )["content"]
        ]

    def _get(self, url: str, params=None) -> dict:
        if params is None:
            params = {}
        resp = self._session.get(url=url, params=params, timeout=10)
        resp.raise_for_status()
        if resp.text == "":
            raise EmptyResponse
        return resp.json()
