import logging
import os
import requests

DISCORD_URL = "https://discord.com/api/v10/channels/962692072941453395/messages"
WEATHER_URL = "https://api.weather.gov/gridpoints/AKQ/44,78/forecast"


def main():
    try:
        content = ""
        forecast = requests.get(WEATHER_URL).json()

        for period in forecast["properties"]["periods"][1:3]:
            content += "{}: {}\n".format(period["name"], period["detailedForecast"])

        content += "React with :soccer: if you're planning on coming!"
        data = {"content": content, "flags": 1 << 12}
        headers = {"Authorization": "Bot " + os.environ["TOKEN"]}
        requests.post(DISCORD_URL, data=data, headers=headers)
    except Exception as exception:
        logging.error(exception)
        raise exception
