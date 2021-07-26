Fixture
========

Fixture is a game that has been played. Has the information for both teams, where it was played and what happened during the match

.. code-block::

    client = APIClient()
    fixture = client.get_fixture(59267)
    # ID of the fixture
    fixture.id
    # 59267

    # Scoreline
    fixture.score
    # "Aston Villa: 2 - Chelsea: 1"

    # Scoreline using team shortnames
    fixture.short_score
    # "Aston Villa: 2 - Chelsea: 1" -

    # Scoreline using the team abbreviations
    fixture.abbr_score1
    # "AVL: 2 - CHE: 1"

    # Amount of events for the fixture
    assert len(fixture.events) == 108

    # Gameweek when the fixture was played
    assert fixture.gameweek == 38

    # Outcome of the fixture. "H" for home team, "A" for away team and None for draw
    fixture.outcome
    # "H"

    # Fixture played a neutral ground
    fixture.neutral
    # False

    # Attendance of the game
    fixture.attendance
    # 10000

    # Name of the winning team
    fixture.winner.name
    # "Aston Villa"

    # Name of the home team
    fixture.homeTeam.name
    # "Aston Villa"

    # ID of the home team
    fixture.homeTeam.id
    # 2

    # City where fixture was played
    fixture.city
    # "Birmingham"

    # Stadium where fixture was played
    fixture.stadium
    # "Villa Park"

    # Total seconds of the fixture
    fixture.seconds
    # 5760

    # Final time
    fixture.time
    # "90 +6'00"


Fixture Event Types
--------------------

These are the known current fixture event types. If you find more then please add them

* free kick won
* free kick lost
* corner
* post
* substitution
* miss
* attempt saved
* goal
* offside
* start (For both first and second half)
* end 1 (End of first half)
* end 2 (End of second half)
* end 14 (End of match)
* attempt blocked
* lineup
* yellow card
* penalty won
* penalty lost
* penalty goal
* contentious referee decisions
* red card