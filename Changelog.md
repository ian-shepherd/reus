# Change Log

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
