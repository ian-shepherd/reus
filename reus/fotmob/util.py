def extract_player_stats(stats):
    mydict = {}

    playerStats = stats[0].get("stats")
    tmp = {}
    for k, v in playerStats.items():
        tmp[k] = v.get("value")
    playerStats = tmp

    mydict["rating"] = playerStats.get("FotMob rating")
    mydict["goals"] = playerStats.get("Goals")
    mydict["assists"] = playerStats.get("Assists")
    mydict["total_shots"] = playerStats.get("Total shots")
    mydict["accurate_passes"] = playerStats.get("Accurate passes")
    mydict["chances_created"] = playerStats.get("Chances created")
    mydict["xG"] = playerStats.get("Expected goals (xG)")
    mydict["xGOT"] = playerStats.get("Expected goals on target (xGOT)")
    mydict["xA"] = playerStats.get("Expected assists (xA)")
    mydict["conceded_penalty"] = playerStats.get("Conceded penalty")
    mydict["fantasy_points"] = playerStats.get("Fantasy points")
    mydict["errors_lead_to_goal"] = playerStats.get("Error led to goal")
    if mydict["errors_lead_to_goal"] is None:
        mydict["errors_lead_to_goal"] = playerStats.get("Errors led to goal")

    try:
        playerStatsAttack = stats[1].get("stats")
        tmp = {}
        for k, v in playerStatsAttack.items():
            tmp[k] = v.get("value")
        playerStatsAttack = tmp

        mydict["shot_accuracy"] = playerStatsAttack.get("Shot accuracy")
        mydict["blocked_shots"] = playerStatsAttack.get("Blocked shots")
        mydict["big_chances_missed"] = playerStatsAttack.get("Big chance missed")
        mydict["touches"] = playerStatsAttack.get("Touches")
        mydict["successful_dribbles"] = playerStatsAttack.get("Successful dribbles")
        mydict["passes_into_final_third"] = playerStatsAttack.get(
            "Passes into final third"
        )
        mydict["accurate_crosses"] = playerStatsAttack.get("Accurate crosses")
        mydict["accurate_long_balls"] = playerStatsAttack.get("Accurate long balls")
        mydict["corners"] = playerStatsAttack.get("Corners")
        mydict["offsides"] = playerStatsAttack.get("Offsides")
        mydict["dispossessed"] = playerStatsAttack.get("Dispossessed")
    except IndexError:
        mydict["touches"] = playerStats.get("Touches")
        mydict["accurate_long_balls"] = playerStats.get("Accurate long balls")

    try:
        playerStatsDefense = stats[2].get("stats")
        tmp = {}
        for k, v in playerStatsDefense.items():
            tmp[k] = v.get("value")
        playerStatsDefense = tmp

        mydict["tackles_won"] = playerStatsDefense.get("Tackles won")
        mydict["blocks"] = playerStatsDefense.get("Blocks")
        mydict["clearances"] = playerStatsDefense.get("Clearances")
        mydict["headed_clearances"] = playerStatsDefense.get("Headed clearance")
        mydict["interceptions"] = playerStatsDefense.get("Interceptions")
        mydict["recoveries"] = playerStatsDefense.get("Recoveries")
        mydict["dribbled_past"] = playerStatsDefense.get("Dribbled past")
    except IndexError:
        pass

    try:
        playerStatsDuels = stats[3].get("stats")
        tmp = {}
        for k, v in playerStatsDuels.items():
            tmp[k] = v.get("value")
        playerStatsDuels = tmp

        mydict["ground_duels_won"] = playerStatsDuels.get("Ground duels won")
        mydict["aerial_duels_won"] = playerStatsDuels.get("Aerial duels won")
        mydict["was_fouled"] = playerStatsDuels.get("Was fouled")
        mydict["fouls_committed"] = playerStatsDuels.get("Fouls committed")
    except IndexError:
        pass

    try:
        mydict["saves"] = playerStats.get("Saves")
        mydict["goals_conceded"] = playerStats.get("Goals conceded")
        mydict["xGOT_faced"] = playerStats.get("xGOT faced")
        mydict["diving_save"] = playerStats.get("Diving save")
        mydict["saves_inside_box"] = playerStats.get("Saves inside box")
        mydict["acted_as_sweeper"] = playerStats.get("Acted as sweeper")
        mydict["punches"] = playerStats.get("Punches")
        mydict["throws"] = playerStats.get("Throws")
        mydict["high_claims"] = playerStats.get("High claim")
        mydict["recoveries"] = playerStats.get("Recoveries")
    except IndexError:
        pass

    return mydict
