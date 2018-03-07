# python-bbcsport-scraper
###### Scrapes football league data from BBC Sport webpages
Currently works for Premier league, Championship, League One and League Two.
Takes data from `"http://www.bbc.co.uk/sport/football/"+league_name+"/table"`

Usage:


```python
# Create LeagueTable object, with the name of the league
league_2 = LeagueTable("league-two")

# Print league table
print(league_2.to_string())

# Get all teams in league, in ranking order
print(league_2.get_team_names())

# Get info from specific team. If team isn't available you'll be shown
# which teams are available. Not case-sensitive
print(league_2.get_team_info("Notts County"))

# Updates league info from webpage. Takes a second or so.
league_2.update_table()

# Returns string url that object is scraping from
league_2.get_league_url()

# Returns string of league name
league_2.get_league_name()
```

The following parameters are available for league_name:

* `premier-league`
* `championship`
* `league-one`
* `league-two`

Example outputs:
```
to_string():

1 team hasn't moved Luton 35 20 9 6 75 35 40 69 WDWDD
2 team hasn't moved Accrington 35 20 6 9 58 38 20 66 WWWDW
3 team has moved up Notts County 36 17 11 8 56 36 20 62 LWDLW
4 team has moved down Wycombe 35 18 8 9 67 51 16 62 DWWLL
5 team hasn't moved Mansfield 35 16 13 6 53 35 18 61 WLWWD
6 team hasn't moved Exeter 33 18 4 11 44 37 7 58 LDLWW
7 team hasn't moved Swindon 35 18 3 14 55 51 4 57 LWLWL
8 team hasn't moved Coventry 34 16 6 12 38 28 10 54 LLLDW
9 team has moved up Lincoln City 35 14 12 9 46 37 9 54 DDWLL
10 team has moved down Carlisle 36 15 9 12 52 45 7 54 LWWWW
11 team has moved up Newport 35 13 12 10 44 45 -1 51 LLLDD
12 team has moved down Crawley 35 15 6 14 41 43 -2 51 WWLWL
13 team has moved down Colchester 35 13 11 11 45 41 4 50 WDWLL
14 team has moved down Cambridge 36 13 10 13 36 46 -10 49 WWWLD
15 team hasn't moved Stevenage 35 11 9 15 46 51 -5 42 LDLWL
16 team hasn't moved Cheltenham 36 10 11 15 48 52 -4 41 DWLLD
17 team hasn't moved Yeovil 34 10 8 16 46 55 -9 38 WDWLL
18 team has moved up Morecambe 34 8 12 14 34 44 -10 36 DLDDW
19 team has moved down Crewe 35 11 3 21 41 57 -16 36 DLWLW
20 team has moved down Forest Green 35 10 6 19 41 59 -18 36 LWWDW
21 team has moved down Grimsby 36 9 9 18 30 53 -23 36 DLLLL
22 team hasn't moved Port Vale 34 9 8 17 37 49 -12 35 DDLLD
23 team hasn't moved Chesterfield 34 8 6 20 35 61 -26 30 LLLLW
24 team hasn't moved Barnet 35 7 8 20 33 52 -19 29 WLDLW


get_team_info():

['3', 'team has moved up', 'Notts County', '36', '17', '11', '8', '56', '36', '20', '62',
'LLost against Barnet on February 10th 2018',
'WWon against Carlisle United on February 13th 2018',
'DDrew against Newport County on February 17th 2018',
'LLost against Cambridge United on February 20th 2018',
'WWon against Stevenage on February 24th 2018', '']

```
