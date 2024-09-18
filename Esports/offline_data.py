import json
import requests


class Offline_Data():
    def __init__(self):
        pass

    def save_offline_data(self, api_link, filename, data=None):
        if api_link and data:
            raise ValueError("You cannot provide both an API link and data. Please provide only one.")

        if not api_link and not data:
            raise ValueError("You must provide either an API link or data.")

        if api_link:
            data = requests.get(api_link).json()

        with open(filename, "w") as file:
            json.dump(data, file)


    def read_offline_data(self, filename):
        with open(filename, "r") as file:
            return json.load(file)
