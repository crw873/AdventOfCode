# %%

# General Imports 
import requests
import pandas as pd
from io import StringIO

# %%

# Puzzle Input URL
url = 'https://adventofcode.com/2022/day/1/input'

# Get the data 
SESSIONID = open('session_id.txt').read()
USER_AGENT = 'crw873'

# Cache the response if already got 
response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

# %%

# Format the data 
input_data = response.text
data_list = input_data.split('\n')
df = pd.read_csv(StringIO(response.text), skip_blank_lines=False, names=['Calories'])
# df.apply(lambda x: )

# %%

# For Loop answer 

# Set some counters 
current_calorie_elf = 0
current_elf_number = 1
max_calorie_elf = {'Number': 0, 'Total Calories': 0}

# Iterate through the list 
for calorie in data_list:
    if calorie == '':
        if current_calorie_elf >= max_calorie_elf['Total Calories']:
            max_calorie_elf['Number'] = current_elf_number
            max_calorie_elf['Total Calories'] = current_calorie_elf
        print(current_elf_number, current_calorie_elf)    
        current_calorie_elf = 0
        current_elf_number += 1
    else:
        current_calorie_elf += int(calorie)

max_calorie_elf
# %%
