from pyLeagueTable import *

l1 = LeagueTable("premier-league")
print(l1.get_team_names())
print(l1.get_team_info("Man Utd"))

league_2 = LeagueTable("league-two")
print(league_2.to_string())
print(league_2.get_team_info("Notts County"))

league_2.update_table()
print("updated")
print(league_2.to_string())

league_2.get_league_url()
league_2.get_league_name()
league_2.to_csv("league.csv")
