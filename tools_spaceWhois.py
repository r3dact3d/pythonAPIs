"""
title: Space Whois
author: Brady Thompson (mailto:redactedtech@gmail.com)
author_url: https://github.com/r3dact3d
version: 0.2.0

This module defines a Tools class that looks up humans in space
"""

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
        url = "http://api.open-notify.org/astros.json"
        response = requests.get(url).json()
        number = response["number"]
        people = response["people"]
        return (
            f"Humans in space currently: {number} and here are details on the {people}"
        )
