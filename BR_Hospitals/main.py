#!/usr/bin/env python3

import os
import requests
import time
import random

url = "https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/Leitos_SUS/Leitos"
data_dir = "./data"
data_file = "Leitos"
file_ext = "csv"
years = list(range(2007, 2027))

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

# Download each year
for year in years:
    file_path = ""

    if year < 2025:
        full_url = f"{url}_{year}.{file_ext}"
        file_path = f"{data_dir}/{data_file}_{year}.{file_ext}"
        print(f"Downloading {file_path}: {full_url}")
        os.system(f"wget {full_url} -O {file_path}")
    else:
        full_url = f"{url}_csv_{year}.zip"
        file_path = f"{data_dir}/{data_file}_{year}.zip"
        print(f"Downloading {file_path}: {full_url}")
        os.system(f"wget {full_url} -O {file_path}")

        # Decompress
        os.system(f"unzip {file_path} -d {data_dir}")
        os.system(f"rm {file_path}")

    time.sleep(random.randint(4, 8)) 

# Encode to UTF8
for filename in os.listdir(data_dir):
    filepath = os.path.join(data_dir, filename)
    if not os.path.isfile(filepath):
        continue

    metadata = os.popen(f"file -i {filepath}").read().strip()
    charset = metadata.split("charset=")[1].upper()
    print(f"Coverting {filepath}:{charset} to UTF-8")
    if "ISO-8859" in charset:
        os.system(f"iconv -f {charset} -t UTF-8 {filepath} > tmp")
    else: 
        os.system(f"iconv -t UTF-8 {filepath} > tmp")
    os.system(f"rm {filepath}")
    os.system(f"mv tmp {filepath}")

