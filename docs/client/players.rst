Players
=======

Players are objects that contains basic information about a player. Each player has an ID which is used to make the request. ``search_player()`` function will return a list of results of players.


There are two types of player responses, ``SearchPlayer`` and ``Player``. ``Player`` has more stats available then a ``SearchPlayer`` but can only retrieved with a player ID where as search player takes a name and can return the ID.


**All the stats data is likely to change**

Base Player
---------------

Base player is the class that both ``Player`` and ``SearchPlayer`` are based on. All the attributes below are available for both.

.. code-block::

    client = APIClient()
    example_player = client.get_player(13286)

    # Player id (int)
    example_player.id

    # Position player plays. Can be G, D, M, F. (str)
    assert example_player.position
    # "F"

    # Shirt number worn by player. (int)
    assert example_player.shirtNumber == 18

    # More detailed position information. (str)
    assert example_player.positionInfo
    # "Centre Striker"

    # If the player is loaned. (bool)
    example_player.loan
    # True

    # Nation they play for. (str)
    example_player.nationalTeam.country
    # England

    # Demonym of their nation team
    example_player.nationalTeam.demonym
    # English

    # ISO of their national time
    example_player.nationalTeam.iso_code
    # "GB-ENG"

    # Country they were born in
    example_player.birthCountry.country
    # "England"

    # Demonym of their birth country
    example_player.birthCountry.demonym
    # "English"

    # ISO code of their birth country
    example_player.birthCountry.iso_code
    # "GB-ENG"

    # Player's birthday
    example_player.birthday
    # "2 October 1997"

    # Player's birthday expressed in epoch milliseconds
    example_player.birthtime
    # 875750400000

    # Player's age represented as years and days
    example_player.age
    # "23 years 285 days"

    # City where the player was born
    example_player.birthplace
    # "London"

    # Player's full name
    example_player.fullName
    # "Tammy Abraham"

    # Player's first name
    example_player.firstName
    # "Tammy"

    # Player's last name
    example_player.lastName
    # "Abraham"



Player
------

The player class has stats that can be generated. There are a ton a stats but unfortunately they are not labeled well. There are something like 150 different stats for players

.. code-block::

    client = APIClient()
    example_player = client.get_player(13286)

    # Generate stats for the player. By default stats are not generated because it handles 100+ attributes.
    example_player.generate_stats()

    # Name of the stat which is also the attribute name
    example_player.accurate_back_zone_pass.name
    # "accurate_back_zone_pass"

    # Description of the stats. For the most part it is just "Todo: <name of stat>"
    example_player.accurate_back_zone_pass.description
    # "Todo: accurate_back_zone_pass"

    # Additional information of the stat. Mostly just empty
    example_player.accurate_back_zone_pass.additionalInfo
    # {}

    # Value of the stat. (int)
    example_player.accurate_back_zone_pass.value
    # 268

    # Can generate all stats when getting the player as well
    example_player2 = client.get_player(13287, generate_stats=True)


SearchPlayer
-------------

Search player has basic additional stats.


.. code-block::

    client = APIClient()
    example_players = client.search_player("Saka")[0]

    # Player ID. Can use to get full stats
    example_player.id
    # 49481

    # Height of player in cm
    example_player.height
    # 178

    # Weight of player in kg
    example_player.weight
    # 65

    # Number of appearances
    example_player.appearances
    # 117

    # Number of goals
    example_player.goals
    # 23

    # Number of assists
    example_player.assists
    # 30

    # Number of tackles
    example_player.tackles
    # 64

    # Number of shots
    example_player.shots
    # 115

    # Number of key passes
    example_player.keyPasses
    # 60

    # Number of clean sheets
    example_player.cleanSheets
    # 13

    # Number of saves
    example_player.saves
    # None

    # Number of goals conceded
    example_player.goalsConceded
    # None


Positions
----------

These are the positions that have been found using the API. If you find more then please add them here

* Centre Striker