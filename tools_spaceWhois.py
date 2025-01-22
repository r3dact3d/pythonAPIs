"""
title: Space Whois
author: Brady Thompson (mailto:redactedtech@gmail.com)
author_url: https://r3dact3d.github.io
git_url: http://github.com/r3dact3d
version: 0.2.0
description: This module defines a Tools class that looks up humans in space
"""

import requests
from pydantic import BaseModel, Field
from typing import List


class Tools:
    _valves: 'Tools'.Valves = None
    _user_valves: 'Tools'.UserValves = None

    def __init__(self):
        self._valves = self.Valves()
        self._user_valves = self.UserValves()

    def get_humans_space(self) -> str:
        """
        Get number of humans in space from API response.

        :param url: URL of the API to retrieve data from
        :return: The number of humans in space, a dictionary with the names of humans and crafts, and a list of astronauts
        """
        # ...
        response = requests.get(url).json()
        number_of_people = response.get("number")
        astronauts = [person["name"] for person in response.get("people")]
        crafts = [craft["name"] for craft in response.get("crafts")]
        return f"""
        Give a description of the{number_of_people} humans in space, {astronauts} astronauts, on {crafts} spacecraft."""