import requests
from pydantic import BaseModel, Field


class Tools:
    class Valves(BaseModel):
        pass

    class UserValves(BaseModel):
        pass

    def __init__(self):
        self.valves = self.Valves()
        self.user_valves = self.UserValves()

    def get_humans_space(self) -> str:
        url = 'http://api.open-notify.org/astros.json'
        response = requests.get(url).json()
        number = response["number"]
        people = response["people"]
        return(f"Humans in space currently: {number}")
        for i in range(0, number):
            boat = people[i]["craft"]
            name = people[i]["name"]
            return(f"{name} is on the {boat}.")
