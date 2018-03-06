from pyLeagueTable import *

l1 = LeagueTable("premier-league")
print(l1.get_team_names())
print(l1.get_team_info("Man Utd"))

league_2 = LeagueTable("league-two")
print(league_2.to_string())
print(league_2.get_team_info("Notts County"))