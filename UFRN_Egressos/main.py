#!/usr/bin/env python3

import os
import requests
import time
import random

url = "https://dados.ufrn.br/dataset/5307e9aa-0946-4c0b-9d55-4f4f61aa8542/resource/642af33a-7c9d-41c4-8077-804830f83f09/download/discentes-egressos-"
data_file = "egressos"
data_dir = "./data"
years = list(range(2010, 2012))

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://dados.gov.br/dados/conjuntos-dados/egressos4",
    "Connection": "keep-alive",
})

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

for year in years:
    print(f"Downloading {data_file}_{year}.csv: {url}{year}.csv")
    response = session.get(url+f"{year}.csv")

    if response.status_code == 200:
        with open(f"{data_dir}/{data_file}_{year}.csv", "wb") as file:
            file.write(response.content)
        print(f"{data_file}_{year}.csv downloaded successfully")
    else:
        print(f"Get request failed with status code: {response.status_code}")
        exit(1)

    time.sleep(random.randint(4, 8)) 
