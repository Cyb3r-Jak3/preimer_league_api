Players
=======

Players are classes that contains basic information about a player. They contain a lot of stats.

Each player has an ID which is used to make the request. ``search_player()`` function will return a list of results of players.


Classes
--------

There are two types of player responses, ``SearchPlayer`` and ``Player``. ``Player`` has more stats available then a ``SearchPlayer`` but can only retrieved with a player ID where as search player takes a name and can return the ID.


**All the example stats data is likely to change**

Base Player
************

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
*******

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
*************

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

There are two types of positions. The first is basic and then there is detailed. Basic positions are G, D, M, and F.

Details positions have items like left or right

These are the positions that have been found using the API. If you find more then please add them here


* Left/Centre/Right Winger
* Left/Centre/Right Central Midfielder
* Centre Central Defender
* Left Full Back
* Centre Striker
* Central Midfielder
* Left/Centre/Right Attacking Midfielder
* Centre Central Midfielder
* Centre Defensive Midfielder
* Right Full Back
* Goalkeeper
* Forward
* Winger
* Centre Attacking Midfielder
* Left/Right Winger
* Centre/Right Central Defender
* Left/Centre/Right Second Striker
* Attacking Midfielder
* Defender
* Striker
* Left/Centre Central Defender
* Central Defender
* Midfielder
* Centre/Right Attacking Midfielder
* Right Winger
* Centre/Right Striker
* Left/Centre/Right Striker
* Left/Centre Second Striker
* Left/Centre Full Back
* Left Winger
* Left/Right Central Defender
* Left/Right Attacking Midfielder
* Right Central Midfielder
* Left/Centre Winger
* Centre Second Striker
* Centre/Right Full Back
* Centre Full Back
* Left/Centre/Right Wing Back
* Centre/Right Central Midfielder
* Left/Right Full Back
* Left/Centre Attacking Midfielder
* Right Wing Back
* Left/Centre Central Midfielder
* Left/Centre/Right Central Defender
* Left Attacking Midfielder
* Left/Right Wing Back

Stats
--------

These are the known stat attributes for players

Forward
**********************

 * accurate_back_zone_pass
 * accurate_chipped_pass
 * accurate_cross
 * accurate_cross_nocorner
 * accurate_flick_on
 * accurate_fwd_zone_pass
 * accurate_launches
 * accurate_layoffs
 * accurate_long_balls
 * accurate_pass
 * accurate_pull_back
 * accurate_through_ball
 * accurate_throws
 * aerial_lost
 * aerial_won
 * appearances
 * assist_attempt_saved
 * assist_blocked_shot
 * assist_own_goal
 * assist_penalty_won
 * attempted_tackle_foul
 * attempts_conceded_ibox
 * attempts_conceded_obox
 * attempts_ibox
 * attempts_obox
 * att_assist_openplay
 * att_bx_centre
 * att_bx_left
 * att_bx_right
 * att_cmiss_high
 * att_cmiss_high_left
 * att_cmiss_high_right
 * att_cmiss_left
 * att_cmiss_right
 * att_corner
 * att_fastbreak
 * att_goal_high_centre
 * att_goal_high_left
 * att_goal_high_right
 * att_goal_low_centre
 * att_goal_low_left
 * att_goal_low_right
 * att_hd_goal
 * att_hd_miss
 * att_hd_post
 * att_hd_target
 * att_hd_total
 * att_ibox_blocked
 * att_ibox_goal
 * att_ibox_miss
 * att_ibox_post
 * att_ibox_target
 * att_lf_goal
 * att_lf_target
 * att_lf_total
 * att_lg_centre
 * att_miss_high
 * att_miss_high_left
 * att_miss_high_right
 * att_miss_left
 * att_miss_right
 * att_obox_blocked
 * att_obox_goal
 * att_obox_miss
 * att_obox_target
 * att_obp_goal
 * att_obx_centre
 * att_one_on_one
 * att_openplay
 * att_post_high
 * att_post_left
 * att_rf_goal
 * att_rf_target
 * att_rf_total
 * att_setpiece
 * att_sv_high_centre
 * att_sv_high_left
 * att_sv_high_right
 * att_sv_low_centre
 * att_sv_low_left
 * att_sv_low_right
 * backward_pass
 * ball_recovery
 * big_chance_created
 * big_chance_missed
 * big_chance_scored
 * blocked_pass
 * blocked_scoring_att
 * challenge_lost
 * clean_sheet
 * crosses_18yard
 * crosses_18yardplus
 * dispossessed
 * draws
 * duel_lost
 * duel_won
 * effective_clearance
 * effective_head_clearance
 * fifty_fifty
 * final_third_entries
 * formation_place
 * fouled_final_third
 * fouls
 * fwd_pass
 * game_started
 * goals
 * goals_conceded
 * goals_conceded_ibox
 * goals_conceded_obox
 * goals_openplay
 * goal_assist
 * goal_assist_intentional
 * goal_assist_openplay
 * goal_fastbreak
 * hand_ball
 * head_clearance
 * head_pass
 * hit_woodwork
 * interception
 * interceptions_in_box
 * interception_won
 * leftside_pass
 * long_pass_own_to_opp
 * long_pass_own_to_opp_success
 * losses
 * lost_corners
 * mins_played
 * offside_provoked
 * offtarget_att_assist
 * ontarget_att_assist
 * ontarget_scoring_att
 * open_play_pass
 * outfielder_block
 * overrun
 * own_goals
 * passes_left
 * passes_right
 * penalty_won
 * pen_area_entries
 * pen_goals_conceded
 * poss_lost_all
 * poss_lost_ctrl
 * poss_won_att_3rd
 * poss_won_def_3rd
 * poss_won_mid_3rd
 * post_scoring_att
 * put_through
 * rightside_pass
 * shield_ball_oop
 * shot_fastbreak
 * shot_off_target
 * six_yard_block
 * successful_fifty_fifty
 * successful_final_third_passes
 * successful_open_play_pass
 * successful_put_through
 * times_tackled
 * total_att_assist
 * total_back_zone_pass
 * total_chipped_pass
 * total_clearance
 * total_contest
 * total_cross
 * total_cross_nocorner
 * total_distance_in_m
 * total_fastbreak
 * total_final_third_passes
 * total_flick_on
 * total_fwd_zone_pass
 * total_launches
 * total_layoffs
 * total_long_balls
 * total_offside
 * total_pass
 * total_pull_back
 * total_scoring_att
 * total_sub_off
 * total_sub_on
 * total_tackle
 * total_through_ball
 * total_throws
 * touches
 * touches_in_opp_box
 * turnover
 * unsuccessful_touch
 * was_fouled
 * winning_goal
 * wins
 * won_contest
 * won_corners
 * won_tackle
 * yellow_card


Midfielder
**********************

 * accurate_back_zone_pass
 * accurate_chipped_pass
 * accurate_corners_intobox
 * accurate_cross
 * accurate_cross_nocorner
 * accurate_flick_on
 * accurate_freekick_cross
 * accurate_fwd_zone_pass
 * accurate_launches
 * accurate_layoffs
 * accurate_long_balls
 * accurate_pass
 * accurate_through_ball
 * accurate_throws
 * aerial_lost
 * aerial_won
 * appearances
 * assist_pass_lost
 * attempted_tackle_foul
 * attempts_conceded_ibox
 * attempts_conceded_obox
 * attempts_ibox
 * attempts_obox
 * att_assist_openplay
 * att_assist_setplay
 * att_bx_centre
 * att_bx_left
 * att_bx_right
 * att_cmiss_high
 * att_fastbreak
 * att_freekick_miss
 * att_freekick_target
 * att_freekick_total
 * att_goal_low_centre
 * att_goal_low_left
 * att_goal_low_right
 * att_hd_goal
 * att_hd_total
 * att_ibox_blocked
 * att_ibox_goal
 * att_ibox_miss
 * att_lf_target
 * att_lf_total
 * att_miss_high
 * att_miss_high_left
 * att_miss_high_right
 * att_miss_left
 * att_miss_right
 * att_obox_blocked
 * att_obox_miss
 * att_obox_target
 * att_obx_centre
 * att_openplay
 * att_pen_goal
 * att_rf_goal
 * att_rf_target
 * att_rf_total
 * att_setpiece
 * att_sv_low_centre
 * att_sv_low_left
 * att_sv_low_right
 * backward_pass
 * ball_recovery
 * big_chance_created
 * big_chance_scored
 * blocked_cross
 * blocked_pass
 * blocked_scoring_att
 * challenge_lost
 * clean_sheet
 * corner_taken
 * crosses_18yard
 * crosses_18yardplus
 * dangerous_play
 * dispossessed
 * draws
 * duel_lost
 * duel_won
 * effective_blocked_cross
 * effective_clearance
 * effective_head_clearance
 * final_third_entries
 * formation_place
 * fouled_final_third
 * fouls
 * freekick_cross
 * fwd_pass
 * game_started
 * goals
 * goals_conceded
 * goals_conceded_ibox
 * goals_conceded_obox
 * goals_openplay
 * goal_assist
 * goal_assist_intentional
 * goal_assist_openplay
 * hand_ball
 * head_clearance
 * head_pass
 * interception
 * interceptions_in_box
 * interception_won
 * leftside_pass
 * long_pass_own_to_opp
 * long_pass_own_to_opp_success
 * losses
 * lost_corners
 * mins_played
 * offtarget_att_assist
 * ontarget_att_assist
 * ontarget_scoring_att
 * open_play_pass
 * outfielder_block
 * overrun
 * passes_left
 * passes_right
 * pen_area_entries
 * pen_goals_conceded
 * poss_lost_all
 * poss_lost_ctrl
 * poss_won_att_3rd
 * poss_won_def_3rd
 * poss_won_mid_3rd
 * put_through
 * rightside_pass
 * shield_ball_oop
 * shot_fastbreak
 * shot_off_target
 * six_yard_block
 * successful_final_third_passes
 * successful_open_play_pass
 * successful_put_through
 * total_att_assist
 * total_back_zone_pass
 * total_chipped_pass
 * total_clearance
 * total_contest
 * total_corners_intobox
 * total_cross
 * total_cross_nocorner
 * total_distance_in_m
 * total_fastbreak
 * total_final_third_passes
 * total_flick_on
 * total_fwd_zone_pass
 * total_launches
 * total_layoffs
 * total_long_balls
 * total_offside
 * total_pass
 * total_scoring_att
 * total_sub_off
 * total_sub_on
 * total_tackle
 * total_through_ball
 * total_throws
 * touches
 * touches_in_opp_box
 * turnover
 * unsuccessful_touch
 * was_fouled
 * wins
 * won_contest
 * won_corners
 * won_tackle
 * yellow_card

Defender
**********************

 * accurate_back_zone_pass
 * accurate_chipped_pass
 * accurate_corners_intobox
 * accurate_cross
 * accurate_cross_nocorner
 * accurate_flick_on
 * accurate_fwd_zone_pass
 * accurate_launches
 * accurate_layoffs
 * accurate_long_balls
 * accurate_pass
 * accurate_pull_back
 * accurate_through_ball
 * accurate_throws
 * aerial_lost
 * aerial_won
 * appearances
 * assist_own_goal
 * attempted_tackle_foul
 * attempts_conceded_ibox
 * attempts_conceded_obox
 * attempts_ibox
 * attempts_obox
 * att_assist_openplay
 * att_assist_setplay
 * att_bx_centre
 * att_bx_left
 * att_bx_right
 * att_cmiss_high
 * att_cmiss_high_left
 * att_cmiss_high_right
 * att_cmiss_left
 * att_cmiss_right
 * att_corner
 * att_fastbreak
 * att_goal_high_right
 * att_goal_low_centre
 * att_goal_low_right
 * att_hd_goal
 * att_hd_miss
 * att_hd_post
 * att_hd_target
 * att_hd_total
 * att_ibox_blocked
 * att_ibox_goal
 * att_ibox_miss
 * att_ibox_post
 * att_ibox_target
 * att_lf_total
 * att_lg_centre
 * att_miss_high
 * att_miss_high_left
 * att_miss_high_right
 * att_miss_left
 * att_miss_right
 * att_obox_blocked
 * att_obox_miss
 * att_obox_target
 * att_obx_centre
 * att_openplay
 * att_post_high
 * att_rf_goal
 * att_rf_target
 * att_rf_total
 * att_setpiece
 * att_sv_high_centre
 * att_sv_high_right
 * att_sv_low_centre
 * att_sv_low_left
 * att_sv_low_right
 * backward_pass
 * ball_recovery
 * big_chance_created
 * big_chance_missed
 * big_chance_scored
 * blocked_cross
 * blocked_pass
 * blocked_scoring_att
 * challenge_lost
 * clean_sheet
 * clearance_off_line
 * corner_taken
 * crosses_18yard
 * crosses_18yardplus
 * dangerous_play
 * dispossessed
 * draws
 * duel_lost
 * duel_won
 * effective_blocked_cross
 * effective_clearance
 * effective_head_clearance
 * error_lead_to_goal
 * error_lead_to_shot
 * fifty_fifty
 * final_third_entries
 * formation_place
 * fouled_final_third
 * fouls
 * foul_throw_in
 * freekick_cross
 * fwd_pass
 * game_started
 * goals
 * goals_conceded
 * goals_conceded_ibox
 * goals_conceded_obox
 * goals_openplay
 * goal_assist
 * goal_assist_intentional
 * goal_assist_openplay
 * goal_assist_setplay
 * hand_ball
 * head_clearance
 * head_pass
 * hit_woodwork
 * interception
 * interceptions_in_box
 * interception_won
 * last_man_tackle
 * leftside_pass
 * long_pass_own_to_opp
 * long_pass_own_to_opp_success
 * losses
 * lost_corners
 * mins_played
 * offside_provoked
 * offtarget_att_assist
 * ontarget_att_assist
 * ontarget_scoring_att
 * open_play_pass
 * outfielder_block
 * overrun
 * own_goals
 * passes_left
 * passes_right
 * penalty_conceded
 * pen_area_entries
 * pen_goals_conceded
 * poss_lost_all
 * poss_lost_ctrl
 * poss_won_att_3rd
 * poss_won_def_3rd
 * poss_won_mid_3rd
 * post_scoring_att
 * put_through
 * red_card
 * rightside_pass
 * shield_ball_oop
 * shot_fastbreak
 * shot_off_target
 * six_yard_block
 * successful_fifty_fifty
 * successful_final_third_passes
 * successful_open_play_pass
 * successful_put_through
 * times_tackled
 * total_att_assist
 * total_back_zone_pass
 * total_chipped_pass
 * total_clearance
 * total_contest
 * total_corners_intobox
 * total_cross
 * total_cross_nocorner
 * total_distance_in_m
 * total_fastbreak
 * total_final_third_passes
 * total_flick_on
 * total_fwd_zone_pass
 * total_launches
 * total_layoffs
 * total_long_balls
 * total_offside
 * total_pass
 * total_pull_back
 * total_scoring_att
 * total_sub_off
 * total_sub_on
 * total_tackle
 * total_through_ball
 * total_throws
 * touches
 * touches_in_opp_box
 * turnover
 * unsuccessful_touch
 * was_fouled
 * winning_goal
 * wins
 * won_contest
 * won_corners
 * won_tackle
 * yellow_card

Goalkeeper
**********************

 * accurate_back_zone_pass
 * accurate_chipped_pass
 * accurate_fwd_zone_pass
 * accurate_goal_kicks
 * accurate_keeper_sweeper
 * accurate_keeper_throws
 * accurate_launches
 * accurate_long_balls
 * accurate_pass
 * accurate_throws
 * aerial_lost
 * aerial_won
 * appearances
 * attempted_tackle_foul
 * attempts_conceded_ibox
 * attempts_conceded_obox
 * att_assist_openplay
 * att_assist_setplay
 * ball_recovery
 * blocked_pass
 * challenge_lost
 * clean_sheet
 * cross_not_claimed
 * dive_catch
 * dive_save
 * diving_save
 * draws
 * duel_lost
 * duel_won
 * effective_clearance
 * effective_head_clearance
 * error_lead_to_goal
 * error_lead_to_shot
 * fifty_fifty
 * final_third_entries
 * formation_place
 * fouls
 * fwd_pass
 * game_started
 * gk_smother
 * goals_conceded
 * goals_conceded_ibox
 * goals_conceded_obox
 * goal_kicks
 * good_high_claim
 * hand_ball
 * head_clearance
 * head_pass
 * interception
 * interceptions_in_box
 * interception_won
 * keeper_pick_up
 * keeper_throws
 * last_man_tackle
 * leftside_pass
 * long_pass_own_to_opp
 * long_pass_own_to_opp_success
 * losses
 * lost_corners
 * mins_played
 * offside_provoked
 * offtarget_att_assist
 * ontarget_att_assist
 * open_play_pass
 * outfielder_block
 * passes_left
 * passes_right
 * penalty_conceded
 * penalty_faced
 * penalty_save
 * pen_area_entries
 * pen_goals_conceded
 * poss_lost_all
 * poss_lost_ctrl
 * poss_won_def_3rd
 * poss_won_mid_3rd
 * punches
 * put_through
 * red_card
 * rightside_pass
 * saved_ibox
 * saved_obox
 * saves
 * shield_ball_oop
 * stand_catch
 * stand_save
 * successful_final_third_passes
 * successful_open_play_pass
 * successful_put_through
 * times_tackled
 * total_att_assist
 * total_back_zone_pass
 * total_chipped_pass
 * total_clearance
 * total_contest
 * total_distance_in_m
 * total_final_third_passes
 * total_fwd_zone_pass
 * total_high_claim
 * total_keeper_sweeper
 * total_launches
 * total_long_balls
 * total_pass
 * total_sub_on
 * total_tackle
 * total_throws
 * touches
 * touches_in_opp_box
 * turnover
 * unsuccessful_touch
 * was_fouled
 * winning_goal
 * wins
 * won_contest
 * won_corners
 * won_tackle
 * yellow_card

