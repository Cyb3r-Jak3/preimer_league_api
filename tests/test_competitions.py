import inspect

import premier_league_api


def test_known_comp():
    comp = premier_league_api.competitions.EN_PR
    assert comp.level == "SEN"
    assert comp.id == 1
    assert comp.source == ""
    assert comp.abbreviation == "EN_PR"
    assert comp.get_season_by_label(label="2021/22") == 418
    assert comp.seasons["2020/21"] == 363


def test_comps():
    for _, comp in inspect.getmembers(premier_league_api.competitions, inspect.isclass):
        assert len(comp.seasons) != 0
        assert isinstance(comp.level, str)
        assert isinstance(comp.id, int)
        assert isinstance(comp.source, str)
        assert isinstance(comp.abbreviation, str)
        assert isinstance(comp.seasons, dict)
        assert callable(comp.get_season_by_label)
