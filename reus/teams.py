import json
import requests

def load_data():
    """Return a list of dictionaries for over all teams in the dataset"""

    url = 'https://raw.githubusercontent.com/ian-shepherd/reus/main/data/teams.json'
    resp = requests.get(url)
    data = json.loads(resp.text)
    
    return data


def attributes():
    """Return a set of available attributes"""
    return {k for d in load_data() for k in d.keys()}


def leagues():
    """Return a set of leagues in the dataset"""
    return set(map(lambda d: d['League'], load_data()))


def teams(league='All'): #league
    """Return a set of teams in the dataset unless filtered for league"""
    
    if league == 'All':
        return set(map(lambda d: d['TeamShort'], load_data()))
    elif isinstance(league, list):
        filtered_teams = list(filter(lambda team: team['League'] in league, load_data()))
        return set(map(lambda d: d['TeamShort'], filtered_teams))
    else:
        filtered_teams = list(filter(lambda team: team['League'] == league, load_data()))
        return set(map(lambda d: d['TeamShort'], filtered_teams))


def team_data(name):
    """Return a dictionary of team data"""
    try:
        return list(filter(lambda team: team['TeamShort'] == name, load_data()))[0]
    except:
        print('Team does not exist in dataset. Use teams() to get set of available teams')


def team_attr(team, attr, colour = 'All'):
    """Return an attribute from a team"""
    data = team_data(team).get(attr)
    if (attr != 'TeamColours') | (colour == 'All'):
        return data
    elif colour == 'Primary':
        return data[0]
    elif colour == 'Secondary':
        return data[1]
    elif colour == 'Alternate':
        try:
            return data[2]
        except:
            return None
    else:
        return data
