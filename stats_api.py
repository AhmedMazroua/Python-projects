# a script that retrieves desired sport, and respected league dynamically and displays stats via api in terminal
from requests import get
from pprint import PrettyPrinter

sports = { "basketball": "nba",
          "football": "nfl",
            "baseball": "mlb",
              "hockey": "nhl"}



sport = input("Desired sport: ").lower()
league = input("Desired league: ").lower()

# api url -> "https://site.api.espn.com/apis/site/v2/sports/{sports}/{nba}/teams"

printer = PrettyPrinter()

data = get(f"https://site.api.espn.com/apis/site/v2/sports/{sport}/{league}/teams").json()

printer.pprint(data)