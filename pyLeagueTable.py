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
        '''
        instantiation of league table array.
        self.league_table is a 2d array where each item is a list of values from the webpage
        self.league_table[0] is the 1st team in the league,
        self.league_table[0][2] is the name of the 1st team in the league.
        '''
        self.league_name = league_name
        self.page = "http://www.bbc.co.uk/sport/football/" + league_name + "/table"
        self.league_table = []
        self.update_table()
        self.all_teams = self.get_team_names()

    def update_table(self):
        page = open_page(self.page)
        soup = bs(page, 'html.parser')
        table = soup.find("tbody", attrs={"class": "gel-long-primer"})
        self.league_table = []
        for a in range(int(get_league_size(str(self.league_name)))):
            team_stats = []
            for i in range(11):
                # Grab the first 10 columns, add to list of table
                team_stats.append(table.find("td", attrs={"data-reactid":(get_league_code(soup)+".$row-"+str(a)+".$td-"+str(i))}).text)

            # Because of the way column 11 is stored (team form over last 5 games)
            # the data needs to be split into a list then appended to the team stats
            # to access the L/D/W characters (minus the opposing team), all that's needed is:
            # get_team_info(team_name)[col][0] where col = 11,12,13,14,15, example is in to_string() function.
            team_form = (table.find("td", attrs={"data-reactid": get_league_code(soup) + ".$row-" + str(a) + ".$td-11"}).text).split(".")
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

    def get_league_name(self):
        return self.league_name

    def get_league_url(self):
        return self.page

    def to_string(self):
        table_str = ""
        for row in self.league_table:
            line_string = ""
            for col in range(11):
                line_string += row[col]
                line_string += " "
            for col in range(11, 16):
                line_string += row[col][0]
            line_string += "\n"
            table_str += line_string
        return table_str

    def to_csv(self, filename: str):
        ''' Writes self.league_table to csv file
        TypeError if filename is not string.
        '''
        try:
            filename.replace(" ", "_")
        except TypeError:
            print("filename isn't a string, please give a string")
        import csv
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            for line in self.league_table:
                writer.writerow(line)
