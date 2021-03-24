[![PyPI version fury.io](https://badge.fury.io/py/reus.svg)](https://pypi.org/project/reus/) [![Lifecycle:
experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental) [![Twitter
Follow](https://img.shields.io/twitter/follow/ishep123?style=social)](https://twitter.com/ishep123) [![Twitter
Follow](https://img.shields.io/twitter/follow/theFirmAISports?style=social)](https://twitter.com/theFirmAISports)


## Soccer/Football Team Information

This package contains general team information such as team name, domestic league country, domestic league, team colours, transfermarkt ID, stadium, and stadium address. A vast majority of the information is from transfermarkt with the exception of a few clubs they did not have colours for that I found in various sources.

## Installation

You can install reus from [PyPi](https://pypi.org/project/reus/) with:

``` python
pip install reus
```

Then to import the package:

``` python
import reus
```


## Examples

#### Load Data

Return a list of dictionaries for over all teams in the dataset

``` python
reus.load_data()
```

#### Attributes

Return a set of available attributes

``` python
reus.attributes()
```

#### Leagues

Return a set of leagues in the dataset

``` python
reus.leagues()
```

#### Teams

Return a set of teams in the dataset unless filtered for league

``` python
reus.teams()
```

#### Team Data

Return a dictionary of team data

``` python
reus.team_data('Borussia Dortmund')
```

#### Team Attributes

Return an attribute from a team

``` python
reus.team_attr('Borussia Dortmund', attr='TeamColours')
```


## Special Thanks

  - To the [FC Python](https://twitter.com/FC_Python) who provided a lot of the initial data and motivation to put this together\!