import requests
from unidecode import unidecode
from offline_data import Offline_Data

class Underdog:
    UNDERDOG_SPORT_IDS = ["ESPORTS", "CS", "CS2", "DOTA2", "VAL", "LOL"]

    def __init__(self):
        self.underdog_data = self.use_offline_data(filename="UD_Offline_data.json")
        self.esports_data = []

    # Use for testing.
    def use_offline_data(self, filename, api_link=None, read=True, write=False, data=None):
        offline_data = Offline_Data()

        if read:
           return offline_data.read_offline_data(filename)

        if write:
            offline_data.save_offline_data(api_link, filename, data)

    # Rename stat type to align with PrizePick data.
    def rename_stat_type(self, stat_type: str):
        stat_type_map = {
            # Key = Underdog Stat Value / Value = PrizePick Value
            "Headshots on Maps 1+2": "MAPS 1-2 Headshots",
            "Kills on Map 1+2": "MAPS 1-2 Kills",
            "Kills on Map 1": "MAP 1 Kills",
            "Headshots on Map 1": "MAP 1 Headshots"
        }

        return stat_type_map.get(stat_type, None)

    def get_games(self):
        for game in self.underdog_data["games"]:
            if game["sport_id"] in self.UNDERDOG_SPORT_IDS:
                game_details = game["scheduled_at"].split("T")
                game_date = game_details[0]
                game_time = game_details[1]

                self.esports_data.append({
                    "match_id": game["id"],
                    "away_team_id": game["away_team_id"],
                    "home_team_id": game["home_team_id"],
                    "game_date": game_date,
                    "game_time": game_time,
                    "match_title": game["title"],
                    "sport_id": game["sport_id"]
                })

    def get_player_details(self):
        pass


    def get_teams(self, match_title):
        team_list = {}
        # Away will be 0 index, home will be 1 index when splitting.
        # if ":" in match_title:
        #     team_list = game["title"].split(":")[1].split("vs.")
        # else:
        #     team_list = game["title"].split("vs")









ud = Underdog()
ud.get_games()
ud.use_offline_data(filename="Underdog_Data_Test.json",  read=False, write=True, data=ud.esports_data)
