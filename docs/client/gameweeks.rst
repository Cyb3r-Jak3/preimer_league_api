Gameweeks
=========

Gameweeks are informational about the start and stop of a gameweek


.. code-block::

    client = APIClient()
    gameweeks = client.get_gameweeks(418)

    # Amount of gameweeks in the season
    len(gameweeks)
    # 38

    example_gameweek = gameweeks[0]

    # Number that the gameweek is in the season
    example_gameweek.gameweek_num
    # 1

    # ID of the gameweek
    example_gameweek.id
    # 6662

    # Number of matches in the gameweek
    example_gameweek.matches
    # 10

    # Gameweek status
    example_gameweek.status
    # "U"

    # Start time in epoch of the gameweek
    example_gameweek.start.epoch
    # 1628881200000

    # Start time label of the gameweek
    example_gameweek.start.label
    # "Fri 13 Aug 2021, 20:00 BST"

    # GMT offset of the gameweek start
    example_gameweek.start.gmtOffset
    # 1

    # Completeness of the gameweek
    example_gameweek.start.completeness
    # 3

    # End time in epoch of the gameweek
    example_gameweek.end.epoch
    # 1629041400000

    # GMT offset of the gameweek end
    example_gameweek.end.gmtOffset
    # 1

    # End time label of the gameweek
    example_gameweek.end.label
    # "Sun 15 Aug 2021, 16:30 BST"

    # Completeness of the gameweek
    example_gameweek.end.completeness
    # 3

