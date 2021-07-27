import premier_league_api.player
from premier_league_api import APIClient, EmptyResponse
import pytest


def test_client_create():
    client = APIClient()
    assert isinstance(client, APIClient)


def test_player():
    client = APIClient()
    with pytest.raises(EmptyResponse):
        client.get_player(-4)
    example_player = client.get_player(13286)
    assert example_player.id == 13286
    assert example_player.position == "F"
    assert example_player.shirtNumber == 18
    assert example_player.positionInfo == "Centre Striker"
    assert example_player.loan
    assert example_player.nationalTeam.country == "England"
    assert example_player.nationalTeam.demonym == "English"
    assert example_player.nationalTeam.iso_code == "GB-ENG"
    assert example_player.birthCountry.country == "England"
    assert example_player.birthCountry.demonym == "English"
    assert example_player.birthCountry.iso_code == "GB-ENG"
    assert example_player.birthday == "2 October 1997"
    assert example_player.birthtime == 875750400000
    assert isinstance(example_player.age, str)
    assert example_player.birthplace == "London"
    assert example_player.fullName == "Tammy Abraham"
    assert example_player.firstName == "Tammy"
    assert example_player.lastName == "Abraham"
    assert str(example_player) == repr(example_player) == example_player.fullName

    example_player.generate_stats()
    with pytest.warns(UserWarning, match="Attempt to generate stats again"):
        example_player.generate_stats()
    assert example_player.accurate_back_zone_pass.name == "accurate_back_zone_pass"
    assert example_player.accurate_back_zone_pass.description == "Todo: accurate_back_zone_pass"
    assert example_player.accurate_back_zone_pass.additionalInfo == {}
    assert isinstance(example_player.accurate_back_zone_pass.value, int)

    example_player2 = client.get_player(13287, generate_stats=True)
    assert isinstance(example_player2, premier_league_api.player.Player)


def test_player_search():
    client = APIClient()
    example_players = client.search_player("Saka")
    assert len(example_players) == 1
    example_player = example_players[0]
    assert example_player.id == 49481
    assert example_player.height == 178
    assert example_player.weight == 65
    assert isinstance(example_player.appearances, int)
    assert isinstance(example_player.goals, int)
    assert isinstance(example_player.assists, int)
    assert isinstance(example_player.tackles, int)
    assert isinstance(example_player.shots, int)
    assert isinstance(example_player.keyPasses, int)
    assert isinstance(example_player.cleanSheets, int)
    assert example_player.saves is None
    assert example_player.goalsConceded is None
    full_player = client.get_player(example_player.id)
    assert full_player.fullName == example_player.fullName
    assert len(client.search_player("Test")) == 0
    assert len(client.search_player("Adam")) == 30


def test_create_competitions():
    premier_league_api.create_competitions_file()


def test_fixture():
    client = APIClient()
    fixture = client.get_fixture(59267)
    assert fixture.id == 59267
    assert fixture.score == "Aston Villa: 2 - Chelsea: 1"
    assert fixture.short_score == "Aston Villa: 2 - Chelsea: 1"
    assert fixture.abbr_score == "AVL: 2 - CHE: 1"
    assert len(fixture.events) == 108
    assert fixture.gameweek == 38
    assert fixture.outcome == "H"
    assert fixture.winner == fixture.homeTeam
    assert fixture.neutral is False
    assert fixture.attendance == 10000
    assert isinstance(fixture.winner, premier_league_api.shared.Team)
    assert fixture.winner.name == "Aston Villa"
    assert fixture.homeTeam.name == "Aston Villa"
    assert fixture.homeTeam.id == 2
    assert fixture.awayTeam.team_type == "FIRST"
    assert fixture.awayTeam.name == "Chelsea"
    assert fixture.city == "Birmingham"
    assert fixture.stadium == "Villa Park"
    assert fixture.seconds == 5760
    assert fixture.time == "90 +6'00"


def test_fixture_event():
    client = APIClient()
    fixture = client.get_fixture(59267)
    event = fixture.events[2]
    assert event.id == 1566625
    assert event.seconds == 81
    assert event.timeLabel == "02"
    assert event.description == "Foul by Matt Targett (Aston Villa)."
    assert event.type == "free kick lost"
    assert len(event.players) == 1
    assert event.players[0] == 4815
    assert str(event) == "Foul by Matt Targett (Aston Villa)."
    assert repr(event) == "81: Foul by Matt Targett (Aston Villa)."
    fixture = client.get_fixture(59268)
    assert fixture.winner == fixture.awayTeam
    fixture = client.get_fixture(59261)
    assert fixture.winner is None


def test_gameweek():
    client = APIClient()
    gameweek = client.get_gameweek(
        season_id=363,
        gameweek=2
    )
    assert len(gameweek) == 10
    assert isinstance(gameweek[0], premier_league_api.gameweek.GameWeekFixture)
    example_gameweek_fixture = gameweek[0]
    assert example_gameweek_fixture.id == 58912
    assert len(example_gameweek_fixture.goals) == 4
    assert len(example_gameweek_fixture.events) == 0
    example_goal = example_gameweek_fixture.goals[0]
    assert example_goal.type == "G"
    assert example_goal.phase == 1
    assert example_goal.seconds == 420
    assert example_goal.time == "07'00"
    assert example_goal.scorer == 3724
    assert example_goal.assist == 8980
    assert example_gameweek_fixture.goals[1].assist is None
    assert example_goal.description == "G"


def test_gameweeks():
    client = APIClient()
    gameweeks = client.get_gameweeks(418)
    assert len(gameweeks) == 38
    example_gameweek = gameweeks[0]
    assert example_gameweek.gameweek_num == 1
    assert example_gameweek.id == 6662
    assert example_gameweek.matches == 10
    assert example_gameweek.status == "U"
    assert str(example_gameweek) == "Gameweek 1 id: 6662"
    assert repr(example_gameweek) == "Gameweek 1 id: 6662"

    assert example_gameweek.start.epoch == 1628881200000
    assert example_gameweek.start.label == "Fri 13 Aug 2021, 20:00 BST"
    assert example_gameweek.start.gmtOffset == 1
    assert example_gameweek.start.completeness == 3

    assert example_gameweek.end.epoch == 1629041400000
    assert example_gameweek.end.gmtOffset == 1
    assert example_gameweek.end.label == "Sun 15 Aug 2021, 16:30 BST"
    assert example_gameweek.end.completeness == 3


def test_teams():
    client = APIClient()
    teams = client.get_teams_in_season(418)
    assert len(teams) == 20
    example_team = teams[0]
    assert example_team.id == 1
    assert example_team.name == "Arsenal"
    assert example_team.team_type == "FIRST"
    assert example_team.abbreviation == "ARS"
    assert example_team.short_name == "Arsenal"
    assert example_team.score is None
