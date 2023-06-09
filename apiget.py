import requests
import os
from datetime import datetime
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()
key = (os.getenv("apikey"))


def currency_rate(currency1, currency2):

    date = datetime.now() - timedelta(days=1)
    year = date.strftime("%Y")
    month = date.strftime("%m")
    day = date.strftime("%d")
    dbtime = year + "-" + month + "-" + day + " " + date.strftime("%H:%M")

    rate_now = requests.get(
        f"https://v6.exchangerate-api.com/v6/{key}/latest/{currency1}"
    ).json()["conversion_rates"][currency2]

    rate_yesterday = requests.get(
        f"https://v6.exchangerate-api.com/v6/{key}/history/{currency1}/{year}/{month}/{day}"
    ).json()["conversion_rates"][currency2]

    if rate_now >= rate_yesterday:
        return ((currency1, currency2, rate_now, dbtime, True))
    else:
        return ((currency1, currency2, rate_now, dbtime, False))
