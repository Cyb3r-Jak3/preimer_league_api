URL Schemes
============

These are the URLS that are used to pull data

Any sort option can be ``asc`` or ``desc``

List Players
-------------

``https://footballapi.pulselive.com/football/players?pageSize=30&compSeasons={Season ID}&altIds=true&page=0&type=player&id=-1&compSeasonId={Season ID}``

Returns a JSON list for players in the given season.

Player stats
-----------------

``https://footballapi.pulselive.com/football/stats/player/{player ID}?comps={competition ID}&compSeasons={Season ID}``

If compSeasons is omitted then all seasons will be returned. Can also just do competition ID.


Competitions
--------------

``https://footballapi.pulselive.com/football/competitions?page=0&pageSize=100&detail=2``

Currently, at 77 competitions. If more are added then an increase in the pageSize will be needed



Competition Seasons
-------------------

``https://footballapi.pulselive.com/football/competitions/{competition ID}/compseasons?page=0&pageSize=100``

Returns a JSON array of the seasons for a given competition.

.. code-block:: json

    {
        [
            {
                "label": "2020/21",
                "id": 363
            }, ...
        ]
    }

Teams
------

``https://footballapi.pulselive.com/football/teams?page=0&pageSize=100&altIds=true&compSeasons={Season ID}``

Returns a JSON array of team objects for a specific season

Fixture Information
-------------------

``https://footballapi.pulselive.com/football/fixtures/{fixture_id}/textstream/{language}``

Returns the fixture information for a game. When changing the language it seems to omit the fixture events


Gameweek
--------

``https://footballapi.pulselive.com/football/fixtures?comps={competition ID}&compSeasons={Season ID}&teams={team IDs. Comma seperated}&page=1&pageSize=10&sort=asc&statuses=C``


There is no way to specifically get a game week. The best way I found was to set the pageSize to half the amount of teams in the league then set the page to the week you want.

Gameweeks
---------

``https://footballapi.pulselive.com/football/compseasons/{Season ID}/gameweeks``

Gets a list of all the gameweeks for a season