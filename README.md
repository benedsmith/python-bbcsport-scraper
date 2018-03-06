# python-bbcsport-scraper
###### Scrapes football league data from BBC Sport webpages
Currently works for Premier league, Championship, League One and League Two.
Takes data from `http://www.bbc.co.uk/sport/football/"+league_name+"/table`

Usage:


```python
# Create LeagueTable object, with the name of the league
league_2 = LeagueTable("league-two")

# Print contents
print(league_2.league_table)

# Get all teams in league, in ranking order
print(league_2.get_team_names())

# Get info from specific team. If team isn't available you'll be shown
# which teams are available. Not case-sensitive
print(league_2.get_team_info("Notts County"))
```

The following parameters are available for league_name:

* `premier-league`
* `championship`
* `league_one`
* `league_two`