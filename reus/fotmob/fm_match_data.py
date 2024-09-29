import datetime as dt
import json
import re
from urllib.request import urlopen


def _extract_events(events, metadata):
    eventList = []
    score = "0:0"
    for e in events:
        mydict = {
            "minute": e.get("time"),
            "minute_stoppage": e.get("overloadTime"),
            "event": e.get("type"),
            "team_id": metadata["id_x"] if e.get("isHome") else metadata["id_y"],
            "score_pre": score,
        }

        if mydict["event"] == "Goal":
            eventDict, score = _extract_goal_event(e)
            mydict = {**mydict, **eventDict}

        elif mydict["event"] == "Card":
            mydict = {**mydict, **_extract_card_event(e, score)}

        elif mydict["event"] == "Substitution":
            mydict = {**mydict, **_extract_subs_event(e, score)}

        elif mydict["event"] == "AddedTime":
            mydict["minutes_added"] = e.get("minutesAddedStr").split()[1]

        elif mydict["event"] == "Half":
            continue

        eventList.append(mydict)

    return eventList


def _extract_goal_event(e):
    mydict = {}
    player1_data = e.get("player")
    mydict["player1"] = player1_data.get("name")
    mydict["player1_id"] = player1_data.get("id")
    mydict["player1_url"] = player1_data.get("profileUrl")

    assist_str = e.get("assistStr")
    mydict["player2"] = (
        re.findall("(?<=assist by ).*$", assist_str)[0] if assist_str else None
    )
    mydict["player2_id"] = e.get("assistPlayerId")
    mydict["player2_url"] = e.get("assistProfileUrl")

    new_score = e.get("newScore")
    mydict["score_post"] = f"{new_score[0]}:{new_score[1]}"
    score = mydict["score_post"]

    mydict["own_goal"] = e.get("ownGoal", False) is not None
    mydict["is_penalty"] = e.get("goalDescription") == "Penalty"
    mydict["is_penalty_shootout"] = e.get("isPenaltyShootoutEvent") is True

    return mydict, score


def _extract_card_event(e, score):
    mydict = {
        "player1": e.get("player").get("name"),
        "player1_id": e.get("player").get("id"),
        "player1_url": e.get("player").get("profileUrl"),
        "card": e.get("card"),
        "score_post": score,
    }

    return mydict


def _extract_subs_event(e, score):
    swap = e.get("swap")
    mydict = {
        "player1": swap[0].get("name"),
        "player1_id": swap[0].get("id"),
        "player1_url": swap[0].get("profileUrl"),
        "player2": swap[1].get("name"),
        "player2_id": swap[1].get("id"),
        "player2_url": swap[1].get("profileUrl"),
        "score_post": score,
    }

    return mydict


def _extract_shootouts(matchFacts, metadata):
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

    return shootoutList


def _extract_shots(shotmap):
    shotList = []
    for shot in shotmap:
        mydict = {
            "id": shot.get("id"),
            "minute": shot.get("min"),
            "minute_stoppage": shot.get("minAdded"),
            "period": shot.get("period"),
            "team_id": shot.get("teamId"),
            "player": shot.get("playerName"),
            "player_id": shot.get("playerId"),
            "situation": shot.get("situation"),
            "shot_type": shot.get("shotType"),
            "outcome": shot.get("eventType"),
            "x": shot.get("x"),
            "y": shot.get("y"),
            "is_blocked": shot.get("isBlocked"),
            "is_on_target": shot.get("isOnTarget"),
            "is_own_goal": shot.get("isOwnGoal"),
            "blocked_x": shot.get("blockedX"),
            "blocked_y": shot.get("blockedY"),
            "goal_crossed_y": shot.get("goalCrossedY"),
            "goal_crossed_z": shot.get("goalCrossedZ"),
            "xG": shot.get("expectedGoals"),
            "xGOT": shot.get("expectedGoalsOnTarget"),
        }
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

    return shotList


def _extract_match_stats(matchStats):
    mydict = {}
    for key, val in matchStats.items():
        period_dict = {}
        for j in val["stats"]:
            stats_dict = {}
            for k in j["stats"]:
                stats_dict[k.get("key")] = k["stats"]
            period_dict[j["key"]] = stats_dict
        mydict[key] = period_dict

    return mydict


def _extract_lineups(lineup, metadata):
    benchPlayerList = []
    startPlayerList = []
    naPlayersList = []

    idx = 0
    for i in [lineup.get("homeTeam"), lineup.get("awayTeam")]:
        team_id = i.get("id")
        for b in i.get("subs"):
            sub_events = b.get("performance").get("substitutionEvents")
            if sub_events is None:
                time_subbed_on = None
                time_subbed_off = None
                subbed_on_reason = None
                subbed_off_reason = None
            elif len(sub_events) == 0:
                time_subbed_on = None
                time_subbed_off = None
                subbed_on_reason = None
                subbed_off_reason = None
            elif len(sub_events) == 1:
                time_subbed_on = sub_events[0].get("time")
                time_subbed_off = None
                subbed_on_reason = sub_events[0].get("reason")
                subbed_off_reason = None
            else:
                time_subbed_on = sub_events[0].get("time")
                time_subbed_off = sub_events[1].get("time")
                subbed_on_reason = sub_events[0].get("reason")
                subbed_off_reason = sub_events[1].get("reason")
            mydict = {
                "team_id": team_id,
                "opta_id": b.get("optaId"),
                "player_id": b.get("id"),
                "player_name": b.get("name"),
                "shirt_number": b.get("shirtnumber"),
                "time_subbed_on": time_subbed_on,
                "time_subbed_off": time_subbed_off,
                "subbed_on_reason": subbed_on_reason,
                "subbed_off_reason": subbed_off_reason,
                "usual_position": b.get("usualPlayingPositionId"),
                "role": "sub",
                "is_captain": b.get("isCaptain"),
            }

            benchPlayerList.append(mydict)

        try:
            metadata = {**metadata, **_extract_managers(i, idx)}
        except TypeError:
            pass
        _extract_managers(i, idx)

        for j in i.get("starters"):
            sub_events = j.get("performance").get("substitutionEvents")
            if sub_events is None:
                time_subbed_on = None
                time_subbed_off = None
                subbed_on_reason = None
                subbed_off_reason = None
            elif len(sub_events) == 0:
                time_subbed_on = None
                time_subbed_off = None
                subbed_on_reason = None
                subbed_off_reason = None
            elif len(sub_events) == 1:
                time_subbed_on = None
                time_subbed_off = sub_events[0].get("time")
                subbed_on_reason = None
                subbed_off_reason = sub_events[0].get("reason")
            mydict = {
                "team_id": team_id,
                "opta_id": j.get("optaId"),
                "player_id": j.get("id"),
                "player_name": j.get("name"),
                "shirt_number": j.get("shirtNumber"),
                "time_subbed_off": time_subbed_off,
                "subbed_off_reason": subbed_off_reason,
                "position": j.get("positionId"),
                "usual_position": j.get("usualPlayingPositionId"),
                "horizontal_layout": j.get("horizontalLayout"),
                "vertical_layout": j.get("verticalLayout"),
                "role": "starter",
                "is_captain": j.get("isCaptain"),
            }

            startPlayerList.append(mydict)

        if i.get("unavailable") is None:
            idx += 1
            continue

        for k in i.get("unavailable"):
            unavailability = k.get("unavailability")
            mydict = {
                "team_id": team_id,
                "player_id": k.get("id"),
                "player_name": k.get("name"),
                "type": unavailability.get("type"),
                "expected_return": unavailability.get("expectedReturn"),
                "injury_id": unavailability.get("injuryId"),
            }

            naPlayersList.append(mydict)

        idx += 1

    return benchPlayerList, startPlayerList, naPlayersList, metadata


def _extract_managers(row, idx):
    mgr = row.get("coach")

    if idx == 0:
        mydict = {
            "manager_x": mgr.get("name"),
            "manager_id_x": mgr.get("id"),
        }
    else:
        mydict = {
            "manager_y": mgr.get("name"),
            "manager_id_y": mgr.get("id"),
        }

    return mydict


def _extract_player_stats(stats):
    mylist = []

    for k, v in stats.items():
        mydict = {}
        mydict["player_id"] = k
        mydict["name"] = v.get("name")

        for j in v["stats"]:
            for k2, v2 in j["stats"].items():
                if v2.get("key") is None:
                    continue
                mydict[v2.get("key")] = v2.get("stat").get("value")

        mylist.append(mydict)

    return mylist


def _extract_lineup_info(lineup):
    if lineup.get("usingOptaLineup"):
        lineup_source = "Opta"
    elif lineup.get("usingEnetpulseLineup"):
        lineup_source = "Enetpulse"
    else:
        lineup_source = "Other"

    mydict = {
        "lineup_source": lineup_source,
        "formation_x": lineup.get("homeTeam").get("formation"),
        "formation_y": lineup.get("awayTeam").get("formation"),
        "team_x_rating": lineup.get("homeTeam").get("rating"),
        "team_y_rating": lineup.get("awayTeam").get("rating"),
    }

    return mydict


def fm_match_data(
    match_id: str, save_json: bool = False, json_file: json = None
) -> tuple:
    """Returns metadata and match data for a given match id

    Args:
        match_id (str): id of a match
        save_json (bool, optional): whether to save json file. Defaults to False.
        json_file (json, optional): json file of match data. Defaults to None.

    Returns:
        tuple: match data
            dict: metadata information
            list: events
            dict: team stats
            list: shots
            list: bench players
            list: starters
            list: players not available
            list: player stats
            list: shootout
            list: momentum
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
    matchStats = content.get("stats").get("Periods")
    shotmap = content.get("shotmap").get("shots")
    lineup = content.get("lineup")
    stats = content.get("playerStats")
    try:
        momentum = content["momentum"]["main"]
    except TypeError:
        momentum = None

    metadata = {
        "id": general.get("matchId"),
        "url": f"/match/{general.get('matchId')}/matchfacts/{data.get('seo').get('path')}",
        "date": dt.datetime.fromisoformat(
            header.get("status").get("utcTime")[:-1] + "+00:00"
        )
        .date()
        .strftime("%Y-%m-%d"),
        "time": dt.datetime.fromisoformat(
            header.get("status").get("utcTime")[:-1] + "+00:00"
        )
        .time()
        .strftime("%H:%M:%S"),
        "league_id": general.get("leagueId"),
        "league": general.get("leagueName"),
        "perent_league_id": general.get("parentLeagueId"),
        "parent_league": general.get("parentLeagueName"),
        "parent_country": general.get("countryCode"),
        "season": general.get("parentLeagueSeason"),
        "matchweek": general.get("matchRound"),
        "team_x": general.get("homeTeam").get("name"),
        "team_y": general.get("awayTeam").get("name"),
        "id_x": general.get("homeTeam").get("id"),
        "id_y": general.get("awayTeam").get("id"),
        "color_x": (
            general.get("teamColors").get("lightMode").get("home")
            if isinstance(general.get("teamColors"), dict)
            else general.get("teamColors")[0].get("color")
        ),
        "color_y": (
            general.get("teamColors").get("lightMode").get("away")
            if isinstance(general.get("teamColors"), dict)
            else general.get("teamColors")[1].get("color")
        ),
        "score_x": header.get("teams")[0].get("score"),
        "score_y": header.get("teams")[1].get("score"),
        "reason": header.get("status").get("reason").get("long"),
        "highlights": (
            matchFacts.get("highlights").get("url")
            if matchFacts.get("highlights")
            else None
        ),
        "venue": matchFacts.get("infoBox").get("Stadium").get("name"),
        "city": matchFacts.get("infoBox").get("Stadium").get("city"),
        "country": matchFacts.get("infoBox").get("Stadium").get("country"),
        "lat": matchFacts.get("infoBox").get("Stadium").get("lat"),
        "long": matchFacts.get("infoBox").get("Stadium").get("long"),
        "referee": matchFacts.get("infoBox").get("Referee").get("text"),
        "attendance": matchFacts.get("infoBox").get("Attendance"),
        "player_of_match": (
            " ".join(matchFacts.get("playerOfTheMatch").get("name").values())
            if matchFacts.get("playerOfTheMatch")
            else None
        ),
        "player_of_match_id": (
            matchFacts.get("playerOfTheMatch").get("id")
            if matchFacts.get("playerOfTheMatch")
            else None
        ),
    }

    events = matchFacts.get("events")["events"]
    eventList = _extract_events(events, metadata)

    shootoutList = _extract_shootouts(matchFacts, metadata)

    shotList = _extract_shots(shotmap)

    teamStats = _extract_match_stats(matchStats)

    benchPlayerList, startPlayerList, naPlayerList, metadata = _extract_lineups(
        lineup, metadata
    )
    metadata = {**metadata, **_extract_lineup_info(lineup)}

    playerStats = _extract_player_stats(stats)

    momentumList = None if momentum is None else momentum.get("data")

    if save_json:
        return (
            metadata,
            eventList,
            teamStats,
            shotList,
            benchPlayerList,
            startPlayerList,
            naPlayerList,
            playerStats,
            shootoutList,
            momentumList,
            data,
        )
    else:
        return (
            metadata,
            eventList,
            teamStats,
            shotList,
            benchPlayerList,
            startPlayerList,
            naPlayerList,
            playerStats,
            shootoutList,
            momentumList,
        )
