import json
from urllib.request import urlopen
import re
import datetime as dt
from .util import extract_player_stats


def fm_match_data(
    match_id: str, save_json: bool = False, json_file: json = None
) -> tuple:
    """Returns metadata and match data for a given match id

    Args:
        match_id (str): id of a match

    Returns:
        tuple: match data
            dict: metadata information
            list: events
            list: shots
            list: bench players
            list starters
            list: players not available
            list: shootout
            json: json file (if save_json=True)
    """

    assert isinstance(match_id, str), "match_id must be a string"

    if json_file is None:
        url = f"https://www.fotmob.com/api/matchDetails?matchId={match_id}"

        response = urlopen(url)
        data = json.loads(response.read())
    else:
        data = json_file

    general = data.get("general")
    header = data.get("header")
    content = data.get("content")
    matchFacts = content.get("matchFacts")
    matchStats = content.get("stats").get("stats")
    shotmap = content.get("shotmap").get("shots")
    lineup = content.get("lineup")

    metadata = {}
    metadata["id"] = general.get("matchId")
    metadata["url"] = (
        "/match/" + metadata["id"] + "/matchfacts/" + data.get("seo").get("path")
    )
    # metadata["date"] = header.get("status").get("startDateStr")
    utcTime = dt.datetime.fromisoformat(
        header.get("status").get("utcTime")[:-1] + "+00:00"
    )
    metadata["date"] = str(utcTime.date())
    # metadata["time"] = matchFacts.get("infoBox").get("Match Date").get("timeFormatted")
    metadata["time"] = str(utcTime.time())
    metadata["league_id"] = general.get("leagueId")
    metadata["league"] = general.get("leagueName")
    metadata["perent_league_id"] = general.get("parentLeagueId")
    metadata["parent_league"] = general.get("parentLeagueName")
    metadata["parent_country"] = general.get("countryCode")
    metadata["season"] = general.get("parentLeagueSeason")
    metadata["matchweek"] = general.get("matchRound")
    metadata["team_x"] = general.get("homeTeam").get("name")
    metadata["team_y"] = general.get("awayTeam").get("name")
    metadata["id_x"] = general.get("homeTeam").get("id")
    metadata["id_y"] = general.get("awayTeam").get("id")
    try:
        metadata["color_x"] = general.get("teamColors").get("home")
        metadata["color_y"] = general.get("teamColors").get("away")
    except AttributeError:
        metadata["color_x"] = general.get("teamColors")[0].get("color")
        metadata["color_y"] = general.get("teamColors")[1].get("color")
    metadata["score_x"] = header.get("teams")[0].get("score")
    metadata["score_y"] = header.get("teams")[1].get("score")
    metadata["reason"] = header.get("status").get("reason").get("long")
    try:
        metadata["highlights"] = matchFacts.get("highlights").get("url")
    except AttributeError:
        metadata["highlights"] = None
    stadium = matchFacts.get("infoBox").get("Stadium")
    metadata["venue"] = stadium.get("name")
    metadata["city"] = stadium.get("city")
    metadata["country"] = stadium.get("country")
    metadata["lat"] = stadium.get("lat")
    metadata["long"] = stadium.get("long")
    metadata["referee"] = matchFacts.get("infoBox").get("Referee").get("text")
    metadata["attendance"] = matchFacts.get("infoBox").get("Attendance")
    try:
        metadata["player_of_match"] = " ".join(
            matchFacts.get("playerOfTheMatch").get("name").values()
        )
        metadata["player_of_match_id"] = matchFacts.get("playerOfTheMatch").get("id")
    except AttributeError:
        metadata["player_of_match"] = None
        metadata["player_of_match_id"] = None

    eventList = []
    events = matchFacts.get("events")["events"]
    score = "0:0"
    for e in events:
        mydict = {}
        mydict["minute"] = e.get("time")
        mydict["minute_stoppage"] = e.get("overloadTime")
        mydict["event"] = e.get("type")
        if e.get("isHome"):
            mydict["team_id"] = metadata["id_x"]
        else:
            mydict["team_id"] = metadata["id_y"]
        mydict["score_pre"] = score

        if mydict["event"] == "Goal":
            mydict["player1"] = e.get("player").get("name")
            mydict["player1_id"] = e.get("player").get("id")
            mydict["player1_url"] = e.get("player").get("profileUrl")
            try:
                mydict["player2"] = re.findall(
                    "(?<=assist by ).*$", e.get("assistStr")
                )[0]
            except TypeError:
                mydict["player2"] = None
            mydict["player2_id"] = e.get("assistPlayerId")
            mydict["player2_url"] = e.get("assistProfileUrl")
            newScore = e.get("newScore")
            mydict["score_post"] = str(newScore[0]) + ":" + str(newScore[1])
            score = mydict["score_post"]
            mydict["own_goal"] = False if e.get("ownGoal") is None else True
            mydict["is_penalty"] = (
                True if e.get("goalDescription") == "Penalty" else False
            )
            mydict["is_penalty_shootout"] = (
                False if e.get("isPenaltyShootoutEvent") is False else True
            )

        elif mydict["event"] == "Card":
            mydict["player1"] = e.get("player").get("name")
            mydict["player1_id"] = e.get("player").get("id")
            mydict["player1_url"] = e.get("player").get("profileUrl")
            mydict["card"] = e.get("card")

        elif mydict["event"] == "Substitution":
            swap = e.get("swap")
            mydict["player1"] = swap[0].get("name")
            mydict["player1_id"] = swap[0].get("id")
            mydict["player1_url"] = swap[0].get("profileUrl")
            mydict["player2"] = swap[1].get("name")
            mydict["player2_id"] = swap[1].get("id")
            mydict["player2_url"] = swap[1].get("profileUrl")
            mydict["score_post"] = score

        elif mydict["event"] == "AddedTime":
            mydict["minutes_added"] = e.get("minutesAddedStr").split()[1]

        elif mydict["event"] == "Half":
            continue

        eventList.append(mydict)

    try:
        shootoutList = []
        penalty_events = matchFacts.get("events")["penaltyShootoutEvents"]
        shootout_score = "0:0"
        for p in penalty_events:
            mydict = {}
            if p.get("isHome"):
                mydict["team_id"] = metadata["id_x"]
            else:
                mydict["team_id"] = metadata["id_y"]
            mydict["event"] = p.get("type")
            mydict["shooter"] = p.get("nameStr")
            mydict["shooter_id"] = p.get("player").get("id")
            mydict["shooter_url"] = p.get("profileUrl")
            mydict["score_pre"] = shootout_score
            try:
                newScore = p.get("penShootoutScore")
                mydict["score_post"] = str(newScore[0]) + ":" + str(newScore[1])
                shootout_score = mydict["score_post"]
            except TypeError:
                mydict["score_post"] = shootout_score

            shootoutList.append(mydict)
    except TypeError:
        shootoutList = None

    stats = {}
    for s in matchStats[1:]:
        for i in s.get("stats"):
            if i.get("stats") != [None, None]:
                if "xG" in i.get("title"):
                    val_x = float(i.get("stats")[0])
                    val_y = float(i.get("stats")[1])
                else:
                    val_x = i.get("stats")[0]
                    val_y = i.get("stats")[1]

                stats[i.get("title").replace(" ", "_").lower() + "_x"] = val_x
                stats[i.get("title").replace(" ", "_").lower() + "_y"] = val_y

    shotList = []
    for shot in shotmap:
        mydict = {}
        mydict["id"] = shot.get("id")
        mydict["minute"] = shot.get("min")
        mydict["minute_stoppage"] = shot.get("minAdded")
        mydict["period"] = shot.get("period")
        mydict["team_id"] = shot.get("teamId")
        mydict["player"] = shot.get("playerName")
        mydict["player_id"] = shot.get("playerId")
        mydict["situation"] = shot.get("situation")
        mydict["shot_type"] = shot.get("shotType")
        mydict["outcome"] = shot.get("eventType")
        mydict["x"] = shot.get("x")
        mydict["y"] = shot.get("y")
        mydict["is_blocked"] = shot.get("isBlocked")
        mydict["is_on_target"] = shot.get("isOnTarget")
        mydict["is_own_goal"] = shot.get("isOwnGoal")
        mydict["blocked_x"] = shot.get("blockedX")
        mydict["blocked_y"] = shot.get("blockedY")
        mydict["goal_crossed_y"] = shot.get("goalCrossedY")
        mydict["goal_crossed_z"] = shot.get("goalCrossedZ")
        mydict["xG"] = shot.get("expectedGoals")
        mydict["xGOT"] = shot.get("expectedGoalsOnTarget")
        on_goal = shot.get("onGoalShot")
        try:
            mydict["on_goal_x"] = on_goal.get("x")
            mydict["on_goal_y"] = on_goal.get("y")
            mydict["on_goal_zoom_ratio"] = on_goal.get("zoomRatio")
        except AttributeError:
            mydict["on_goal_x"] = None
            mydict["on_goal_y"] = None
            mydict["on_goal_zoom_ratio"] = None

        shotList.append(mydict)

    benchPlayerList = []
    startPlayerList = []

    for i in lineup.get("lineup"):
        idx = lineup.get("lineup").index(i)
        team_id = i.get("teamId")
        for b in i.get("bench"):
            mydict = {}
            mydict["team_id"] = team_id
            mydict["opta_id"] = b.get("usingOptaId")
            mydict["player_id"] = b.get("id")
            # mydict["player_name"] = " ".join(b.get("name").values())
            mydict["player_name"] = b.get("name").get("fullName")
            mydict["player_url"] = b.get("pageUrl")
            mydict["shirt_number"] = b.get("shirt")
            mydict["time_subbed_on"] = b.get("timeSubbedOn")
            mydict["time_subbed_off"] = b.get("timeSubbedOff")
            mydict["minutes_played"] = b.get("minutesPlayed")
            mydict["usual_position"] = b.get("usualPosition")
            mydict["role"] = b.get("role")
            mydict["is_captain"] = b.get("isCaptain")
            try:
                statsDict = extract_player_stats(b.get("stats"))
                mydict.update(statsDict)
            except TypeError:
                pass

            benchPlayerList.append(mydict)

        try:
            mgr = i.get("coach")[0]
            if idx == 0:
                # metadata["manager_x"] = " ".join(mgr.get("name").values())
                metadata["manager_x"] = mgr.get("name").get("fullName")
                metadata["manager_id_x"] = mgr.get("id")
                metadata["manager_url_x"] = mgr.get("pageUrl")
            else:
                # metadata["manager_y"] = " ".join(mgr.get("name").values())
                metadata["manager_y"] = mgr.get("name").get("fullName")
                metadata["manager_id_y"] = mgr.get("id")
                metadata["manager_url_y"] = mgr.get("pageUrl")
        except TypeError:
            pass

        for j in i.get("players"):
            for k in j:
                mydict = {}
                mydict["team_id"] = team_id
                mydict["opta_id"] = k.get("usingOptaId")
                mydict["player_id"] = k.get("id")
                mydict["player_name"] = " ".join(k.get("name").values())
                mydict["player_url"] = k.get("pageUrl")
                mydict["shirt_number"] = k.get("shirt")
                mydict["time_subbed_on"] = k.get("timeSubbedOn")
                mydict["time_subbed_off"] = k.get("timeSubbedOff")
                mydict["minutes_played"] = k.get("minutesPlayed")
                mydict["position"] = k.get("positionStringShort")
                mydict["usual_position"] = k.get("usualPosition")
                mydict["role"] = k.get("role")
                mydict["is_captain"] = k.get("isCaptain")
                try:
                    mydict["fantasy_points"] = k.get("fantasyScore").get("num")
                    statsDict = extract_player_stats(k.get("stats"))
                    mydict.update(statsDict)
                except AttributeError:
                    # mydict["fantasy_points"] = None
                    # mydict = {}
                    pass

                startPlayerList.append(mydict)

    if lineup.get("usingOptaLineup"):
        metadata["lineup_source"] = "Opta"
    elif lineup.get("usingEnetpulseLineup"):
        metadata["lineup_source"] = "Enetpulse"
    else:
        metadata["lineup_source"] = "Other"

    metadata["formation_x"] = lineup.get("lineup")[0].get("lineup")
    metadata["formation_y"] = lineup.get("lineup")[1].get("lineup")
    metadata["team_x_rating"] = lineup.get("teamRatings").get("home").get("num")
    metadata["team_y_rating"] = lineup.get("teamRatings").get("away").get("num")

    try:
        matchNaPlayers = lineup.get("naPlayers").get("naPlayersArr")
        naPlayerList = []
        team_id = metadata["id_x"]
        for j in matchNaPlayers:
            for k in j:
                mydict = {}
                mydict["team_id"] = team_id
                mydict["player_id"] = k.get("id")
                mydict["player_name"] = k.get("naInfo").get("name")
                mydict["player_url"] = k.get("pageUrl")
                mydict["reason"] = k.get("naInfo").get("naReason")
                try:
                    mydict["expected_return"] = (
                        k.get("naInfo")
                        .get("expectedReturn")
                        .get("expectedReturnFallback")
                    )
                except AttributeError:
                    mydict["expected_return"] = None
                naPlayerList.append(mydict)
            team_id = metadata["id_y"]
    except AttributeError:
        naPlayerList = None

    if save_json:
        return (
            metadata,
            eventList,
            shotList,
            benchPlayerList,
            startPlayerList,
            naPlayerList,
            shootoutList,
            data,
        )
    else:
        return (
            metadata,
            eventList,
            shotList,
            benchPlayerList,
            startPlayerList,
            naPlayerList,
            shootoutList,
        )
