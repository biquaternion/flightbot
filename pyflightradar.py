#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json


def get_flightradar_data(bounds):
    resp = requests.get('https://data-live.flightradar24.com/'
                        'zones/fcgi/feed.js?',
                        params={'bounds': '{max_lat},'
                                          '{min_lat},'
                                          '{min_lon},'
                                          '{max_lon}'.format(max_lat=bounds[0],
                                                             min_lat=bounds[1],
                                                             min_lon=bounds[2],
                                                             max_lon=bounds[3])},
                        headers={'Content-Type': 'application/json',
                                 'user-agent': 'pyflightradar/0.0.1'})
    # print(resp.content)
    return json.loads(resp.content)


if __name__ == '__main__':
    header = ['id',
              'lat',
              'lon',
              'track',
              'alt',
              'speed',
              'f_06',
              'radar',
              'type',
              'registr',
              'f_10',
              'src',
              'dst',
              'flight',
              'f_14',
              'f_15',
              'callsign',
              'f_17']

    flightradar_data = get_flightradar_data((56.29, 55.13, 36.83, 38.63))
    for key in flightradar_data:
        entry = flightradar_data[key]
        if isinstance(entry, list):
            entry_info = dict(zip(header, entry))
            print(entry_info)
