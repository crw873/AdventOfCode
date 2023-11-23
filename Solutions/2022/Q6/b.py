# %%

# General Imports 
import requests
import pandas as pd
from io import StringIO

# %%

# Puzzle Input URL
url = 'https://adventofcode.com/2022/day/6/input'

# Get the data 
SESSIONID = open('session_id.txt').read()
USER_AGENT = 'crw873'

# Cache the response if already got 
response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

# %%

def get_start_packet_marker(packet, marker_length=14):
    for i in range(len(packet)):
        if len(set(packet[i:i+marker_length])) == marker_length:
            return marker_length + i
    return 'No Marker Found'

get_start_packet_marker(response.text)

# %%
