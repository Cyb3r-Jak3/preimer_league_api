Gameweek
=========

A gameweek is a list of ``GameWeekFixture`` s. A couple of difference between a ``GameWeekFixture`` and a ``Fixture``:
    - ``GameWeekFixture`` has a list of goals scored.
    - ``GameWeekFixture`` does **not** have a list of FixtureEvents. Need to use the id to get the full fixture

.. code-block::

    client = APIClient()
    # Defaults to pulling 10 games
    gameweek = client.get_gameweek(
        season_id=363,
        gameweek=2
    )

    example_gameweek_fixture = gameweek[0]

    # Fixture ID
    example_gameweek_fixture.id
    # 58912

    # Amount of goals in the fixture
    len(example_gameweek_fixture.goals)
    # 4

    example_goal = example_gameweek_fixture.goals[0]

    # Type of goal. Either "G" or "P"
    example_goal.type
    # "G"

    # Phase or half when the goal was scored
    example_goal.phase
    # 1

    # Seconds when goal was scored
    example_goal.seconds
    # 420

    # Clock when the goal was scored
    example_goal.time
    # "07'00"

    # Player ID of the goal scorer
    example_goal.scorer
    # 3724

    # Player ID who assisted. Not always set
    example_goal.assist
    # 8980


Gameweek Goals types
---------------------

* G (goal)
* P (penalty)
