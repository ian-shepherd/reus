# Change Log

## 1.1.3 2023-06-30
* added github actions for testing
* deprecated fm_league_ids and fm_league_urls in favor of fm_leagues
* added season parameter
	* fm_league_matches
	* fm_league_table
	* fm_season_stat_leaders
	* fm_season_stats
* reduced complexity of functions
	* fb_match_keeper_stats
	* fb_match_metadata
	* fb_match_summary
	* fb_match_team_stats
	* fb_seasib_fixtures_urls
	* fb_season_urls
	* fotmob util function
* added error handling to fb_league_table for last 5 matches
* added error handling for age
	* fb_team_player_advanced_keeper_stats
	* fb_team_player_defensive_action_stats
	* fb_team_player_goal_sca_stats
	* fb_team_player_keeper_stats
	* fb_team_player_misc_stats
	* fb_team_player_passing_stats
	* fb_team_player_passing_type_stats
	* fb_team_player_playing_time_stats
	* fb_team_player_possession_stats
	* fb_team_player_shooting_stats
	* fb_team_player_summary_stats
	* tm_player_metadata
	* tm_team_player_data
	* tm_team_transfers
* fixed docstring for fm_match_ids
* fixed currency bug for tm_player_transfers
* added unittests for all functions

## 1.1.2 2023-06-02
* added fotmob functions
	* fm_league_ids: Returns a series of league ids
	* fm_league_matches: Returns matches of a given league
	* fm_league_table: Returns standing of a given league
	* fm_league_urls: Returns a series of league urls for the current season
	* fm_season_stat_leaders: Returns top 3 stat leaders of a given league
	* fm_season_stats: Returns complete list of stat leaders of a given league
* added util functions
	* generate_standings: Returns a dataframe of league standings from given match results
* fm_match_data: fixed player name bug that returned repeat names
* fb_season_fixture_urls: updated documentation
* fb_season_urls: updated documentation

## 1.1.1 2023-05-13
* fb_league_table: fixed broken tags, added Pts/MP and last 5
* fb_match_data: added save_html and html_file arguments and functionality
* fb_match_defensive_actions_stats: updated from StatsBomb to Opta data
* fb_match_keeper_stats: updated from StatsBomb to Opta data
* fb_match_lineups: renamed backend variables to more appropriate name
* fb_match_metadata: 
	* updated error handling for edge case scenarios where one set of missing information (ex. one team missing a captain or manager, incomplete officials info)
	* added league_id, league name, and matchweek
* fb_match_misc_stats: updated from StatsBomb to Opta data
* fb_match_passing_stats: updated from StatsBomb to Opta data
* fb_match_passing_type_stats: updated from StatsBomb to Opta data
* fb_match_possession_stats: updated from StatsBomb to Opta data
* fb_match_shots: updated to include Opta xG data
* fb_match_summary_stats: updated from StatsBomb to Opta data
* fb_match_summary: improved error handling for match events
* fb_match_team_stats: improved error handling for missing stats
* fb_season_fixture_urls: updated arguments from statsbomb flag to advanced data flag
* fb_season_urls: updated arguments from statsbomb flag to advanced data flag
* fb_team_player_advanced_keeper: fixed broken tasks and age error handling
* fb_team_player_defensive_action_stats: updated from StatsBomb to Opta data and age error handling
* fb_team_player_goal_sca_stats: updated from StatsBomb to Opta data and age error handling
* fb_team_player_keeper_stats: updated from StatsBomb to Opta data and age error handling
* fb_team_player_misc_stats: updated from StatsBomb to Opta data and age error handling
* fb_team_player_passing_stats: updated from StatsBomb to Opta data and age error handling
* fb_team_player_passing_type_stats: updated from StatsBomb to Opta data and age error handling
* fb_team_player_playing_time_stats: updated from StatsBomb to Opta data and age error handling
* fb_team_player_possession_stats: updated from StatsBomb to Opta data and age error handling
* fb_team_player_shooting_stats: updated from StatsBomb to Opta data and age error handling
* fb_team_player_summary_stats: updated from StatsBomb to Opta data and age error handling
* added team stat functions
	* fb_team_advanced_keeper_stats
	* fb_team_data
	* fb_team_defensive_actions_stats
	* fb_team_goal_sca_stats
	* fb_team_keeper_stats
	* fb_team_misc_stats
	* fb_team_passing_stats
	* fb_team_passing_type_stats
	* fb_team_playing_time_stats
	* fb_team_possession_stats
	* fb_team_shooting_stats
	* fb_team_summary_stats

## 1.1.0 2022-10-09
Added fotmob functionality for getting match data
Updated function documentation with type hints
Removed repetitive print statements when a match was forfeited

## 1.0.8 2022-08-09
Removed * from score when match forfeited
Added error handling for no manager or captain in fb_match_metadata
Added verbose parameter in fb_match_metadata that prints error when match forfeited or missing manager or captain
Removed main call from fb_match_defensive_actions_stats
Changed ids in fb_match_keeper_stats to match new format
Changed ids in fb_match_shots to match new format

## 1.0.7 2022-07-02 Error handling for forfeited matches and missing player identifier
Renamed dictionary from matadict to metadict in fb_match_metadata
Added error handling for bad names, no csk identifier, in fb_match_summary_stats
Added error handling for no age in fb_match_summary_stats
Added error handling and note for forfeited matches in fb_match_metadata

## 1.0.6 2022-06-21 Bug fix
Added further error handling for fb_match_summary when matches have slightly different syntax around events without a second player (i.e. own goal, penalty kicks, shootouts)

### 1.0.5 2022-06-18 Bug fix
Fbref matches failed on ones with penalty kick goals

### 1.0.4 2022-06-18 Added fbref team functions and minor bug fixes
Removed trailing whitespace from team name in fbref.fb_league_table
Updated bare except to Attribute error in fbref.fb_match_summary
Linted util and all fbref functions
Added url as an argument for fbref functions
Added fbref team functions

### 1.0.3 2022-06-18 Yanked

### 1.0.2 2022-02-11 Fixture Bug fix
Added handling for getting match urls for leagues with playoffs in fbref.fb_match_urls

### 1.0.1 2022-02-11 Bug fix
Fixed spelling of passing in fbref.fb_match_team_stats function
Fixed documentation incorrectly stating argument was a pageSoup object instead of url string

### 1.0.0 2022-01-07 Release v2
Removed limited original functionality
Adding capability to extract fbref and transfermarkt data
Added documentation for GitHub pages

### 0.0.3 2021-03-23 Initial release
Initial json file
Initial functions in teams.py
