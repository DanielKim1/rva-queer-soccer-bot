from datetime import datetime
from logging import error
from os import environ
from zoneinfo import ZoneInfo
import requests

DISCORD_URL = "https://discord.com/api/v10/channels/962692072941453395/messages"
IANA_KEY = "America/New_York"
WEATHER_URL = "https://api.weather.gov/gridpoints/AKQ/44,78/forecast/hourly"


def main():
    try:
        content = ""
        forecast = requests.get(WEATHER_URL).json()

        for period in forecast["properties"]["periods"][11:14]:
            time = (
                datetime.fromisoformat(period["startTime"])
                .astimezone(ZoneInfo(IANA_KEY))
                .timetz()
                .strftime("%I:%M%p")
            )
            content += "{} | {}°F | {}\n".format(
                time, period["temperature"], period["shortForecast"]
            )

        content += "React with :soccer: if you're planning on coming!"
        data = {"content": content, "flags": 4096}
        headers = {"Authorization": "Bot " + environ["TOKEN"]}
        requests.post(DISCORD_URL, data=data, headers=headers)
    except Exception as exception:
        error(exception)
        raise exception
