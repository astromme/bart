#!/usr/bin/env python3

import datetime
import json
import requests
import xmltodict

from api_key import API_KEY
ETD_URL = 'https://api.bart.gov/api/etd.aspx?cmd=etd&orig=ALL&key={api_key}'
OUTPUT_DIR = "output"

from utils import create_dir_if_needed

def main():
    timestamp = '{:%Y-%m-%d.%H-%M-%S}'.format(datetime.datetime.now())

    print("getting estimated time of departure")
    url = ETD_URL.format(api_key=API_KEY)
    print(url)
    r = requests.get(url)
    r_dict = xmltodict.parse(r.text)

    create_dir_if_needed(OUTPUT_DIR)

    filename = '{timestamp}-etd.json'.format(timestamp=timestamp)
    with open(OUTPUT_DIR + '/' + filename, 'w') as f:
        f.write(json.dumps(r_dict, indent=2))

if __name__ == '__main__':
    main()
