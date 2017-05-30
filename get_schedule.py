#!/usr/bin/env python3

import datetime
import json
import os
import requests
import xmltodict

from api_key import API_KEY
ROUTES_URL = 'http://api.bart.gov/api/route.aspx?cmd=routes&key={api_key}'
ROUTE_SCHEDULE_URL = 'http://api.bart.gov/api/sched.aspx?cmd=routesched&route={route_id}&key={api_key}'
OUTPUT_DIR = "output"

from utils import create_dir_if_needed

def main():
    datestamp = '{:%Y-%m-%d}'.format(datetime.datetime.now())

    print("getting today's routes")
    url = ROUTES_URL.format(api_key=API_KEY)
    print(url)
    r = requests.get(url)
    r_dict = xmltodict.parse(r.text)

    create_dir_if_needed(OUTPUT_DIR)

    filename = '{datestamp}-routes.json'.format(datestamp=datestamp)
    with open(OUTPUT_DIR + '/' + filename, 'w') as f:
        f.write(json.dumps(r_dict, indent=2))

    route_ids = []
    for route in r_dict['root']['routes']['route']:
        route_ids.append(route['number'])

    print('route_ids =', route_ids)
    print()

    for route_id in route_ids:
        print("getting schedule for route {}".format(route_id))
        url = ROUTE_SCHEDULE_URL.format(route_id=route_id, api_key=API_KEY)
        print(url)
        r = requests.get(url)
        r_dict = xmltodict.parse(r.text)

        filename = '{datestamp}-route{route_id}-schedule.json'.format(datestamp=datestamp, route_id=route_id)
        with open(OUTPUT_DIR + '/' + filename, 'w') as f:
            f.write(json.dumps(r_dict, indent=2))
        print()

if __name__ == '__main__':
    main()
