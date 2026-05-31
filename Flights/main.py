#!/usr/bin/env python3

import os
import requests
import time
import random

data_file = "flights_january"
data_dir = "./data"
years = list(range(2000, 2003))

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr",
    "Connection": "keep-alive",
})

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

response = session.post("https://transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr")
if response.status_code == 200:
    print("POST request successful.")

    for year in years:
        print(f"Downloading {data_file}_{year}.csv")
        # Link from the file with prezip option enabled
        get_url = f"https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_{year}_10.zip"
        response = session.get(get_url)

        # Check if GET request was successful
        if response.status_code == 200:
            with open(f"{data_dir}/{data_file}_{year}.zip", "wb") as file:
                file.write(response.content)
            print(f"{data_file}_{year}.zip downloaded successfully.")
        else:
            print(f"GET request failed with status code: {response.status_code}")
            exit(1)

        time.sleep(random.randint(4, 8)) 

else:
    print(f"POST request failed with status code: {response.status_code}")
