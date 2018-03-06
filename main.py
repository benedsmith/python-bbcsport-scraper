from bs4 import BeautifulSoup as bs
import urllib.request, urllib


def get_league_code(soup):
    # Check league name is in league codes dict
    try:
        # Grab the body of the table
        tbody = soup.find("tbody", attrs={"class": "gel-long-primer "})
        # Take the value of the reactid
        # This is needed because the value changes every time you visit the page
        # Probably to deter scraping?
        return tbody["data-reactid"]

    except KeyError:
        print("league name not recognised! refer to docs")  # TODO write docs


def get_league_size(league_name):
    league_sizes = {"premier-league": 20, "championship": 24,
                    "league-one": 24, "league-two": 24}
    try:
        league_size = league_sizes[str(league_name)]
        return league_size
    except KeyError:
        print("league name not recognised! refer to docs")  # TODO write docs


def open_page(page_url):
    try:
        return urllib.request.urlopen(page_url)
    except IOError:
        print("URL not opened")


class LeagueTable:
    def __init__(self, league_name):
        page = "http://www.bbc.co.uk/sport/football/"+league_name+"/table"
        page = open_page(page)
        soup = bs(page, 'html.parser')
        table = soup.find("tbody", attrs={"class": "gel-long-primer"})
        self.league_table = []

        for a in range(int(get_league_size(str(league_name)))):
            team_stats = []
            for i in range(11):
                # Grab the first 10 columns, add to list of table
                team_stats.append(table.find("td", attrs={"data-reactid":(get_league_code(soup)+".$row-"+str(a)+".$td-"+str(i))}).text)

            # Because of the way column 11 is stored (team form over last 5 games
            # the data needs to be split into a list then appended to the team stats
            # to access the L/D/W characters (minus the opposing team), all that's needed is:
            # get_team_info(team_name)[col][0] where col = 11,12,13,14,15
            team_form = table.find("td", attrs={"data-reactid": (get_league_code(soup) + ".$row-" + str(a) + ".$td-11")}.text).split(".")
            team_stats += team_form
            self.league_table.append(team_stats)

    def get_team_names(self):
        team_names = []
        for item in self.league_table:
            team_names.append(item[2])
        return team_names

    def get_team_info(self, team_name):
        try:
            for team in self.league_table:
                if team[2].upper() == team_name.upper():
                    return team
        except ValueError:
            print("Team not found! Here are the teams in that league: \n")
            for item in self.get_team_names():
                print(item)


l1 = LeagueTable("premier-league")
# print(l1.league_table)
# print(l1.get_team_names())

print(l1.get_team_info("Man Utd"))

league_2 = LeagueTable("league-two")
print(league_2.get_team_info("Notts County"))