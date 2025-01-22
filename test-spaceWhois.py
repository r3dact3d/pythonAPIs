# Open Astronaut - A Python Module for fetching information about humans currently in space from the OpenAstronaut API.
#
# This module provides a function for retrieving data about astronauts, making it easy to use within AI chatbots, web apps,
# and other projects that require information about human space travel.
#
# Usage: To retrieve information about humans in space, simply call the open_astronaut.get_humans() function:
#
#     from open_astronaut import get_humans
#     astronaut_data = get_humans()
#
# For more details on the API used and its documentation, visit https://open-notify.org/Open-Notify-API/

import requests
from typing import List

def get_humans() -> List[dict]:
    """
    Retrieve a list of dictionaries containing information about humans currently in space from the OpenAstronaut API.

    Returns:
        A list of dictionaries containing astronaut data, including their name, craft, nationality, and ID (if available).
    """
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url).json()
    number_of_people = response["number"]
    astronauts = response["people"]
        
    astronaut_data = []
    for astronaut in astronauts:
        name = astronaut["name"]
        craft = astronaut["craft"]
        astronaut_data.append( f"{name} is currently stationed on {craft}.")
    astronaut_data.append(f"There are {number_of_people} in space right now.")
    return astronaut_data
  
print(get_humans())

        
