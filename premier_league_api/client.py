"""API Client for requests"""
from typing import List
import requests
from .player import Player, SearchPlayer
from .gameweek import GameWeekFixture
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

        :param generate_stats:
        :param player_id:
        :param comp_id:
        :param season_id:
        :return:
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
        Implement pagination fo results
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

    def get_fixture(self, fixture_id: int, language_code: str = "EN") -> FixtureResult:
        """

        :param fixture_id:
        :param language_code:
        :return:
        """
        return FixtureResult(
            self._get(
                url=f"{STANDARD_URL}fixtures/{fixture_id}/textstream/{language_code}",
                params={"pageSize": 500, "sort": "asc"},
            )
        )

    def get_teams_in_season(self, season_id: int) -> List[Team]:
        """

        :param season_id:
        :return:
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
            It should be equal to half the amount of teams. Elimination tornements will be tricky

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
        resp = self._session.get(url=url, params=params)
        resp.raise_for_status()
        if resp.text == "":
            raise EmptyResponse
        return resp.json()
