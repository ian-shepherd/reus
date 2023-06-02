[![PyPI version fury.io](https://badge.fury.io/py/reus.svg)](https://pypi.org/project/reus/) [![Lifecycle:
experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental) [![Twitter
Follow](https://img.shields.io/twitter/follow/ishep123?style=social)](https://twitter.com/ishep123) [![Twitter
Follow](https://img.shields.io/twitter/follow/theFirmAISports?style=social)](https://twitter.com/theFirmAISports)


# Overview

Reus is a Python library that provides a convenient way to scrape soccer data from various sources, including FBref, FotMob, and Transfermarkt. It aims to simplify the process of accessing and analyzing soccer-related information for data enthusiasts and sports analysts.

## Features

- Retrieve detailed soccer statistics, including player and team performance metrics.
- Fetch fixture information for specific seasons and competitions.
- Access transfer market data, including player transfers, contract details, and market values.

## Inspiration

Reus takes inspiration from the R package [worldfootballR](https://github.com/JaseZiv/worldfootballR), and their associated [dataset](https://github.com/JaseZiv/worldfootballR_data), which is known for its extensive soccer data scraping capabilities. While Reus mimics some of the functionalities of worldfootballR, it is designed specifically for Python users, providing similar functionality and ease of use.

## Installation

You can install reus from [PyPi](https://pypi.org/project/reus/) with:

``` python
pip install reus
```

Then to import the package:

``` python
import reus
```

Please scrape responsibly. Do not make calls faster than 1 per 3 seconds. If you are iterating over multiple pages, please use a sleep time of at least 3 seconds.

```python
time.sleep(4)
```

It is a minor inconvenience to you but lets us all keep accessing the data.

More detailed documentation is provided [here](https://ian-shepherd.github.io/reus/)

## Roadmap
  - translation function for players and teams
  - change outputs of fbref functions from lists and tuples to dictionaries
  - fbref player scouting reports
  - transfermarkt team staff
  - transfermarkt staff history
  - understat data


## Resources
  - [FBref](https://fbref.com/)
  - [Fotmob](https://www.fotmob.com/)
  - [Transfermarkt](http://transfermarkt.com/)
  - [FC Python](https://fcpython.com/)
  - [538](https://fivethirtyeight.com/)