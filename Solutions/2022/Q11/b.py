# %%

# General Imports 
import requests
import pandas as pd
from io import StringIO
import numpy as np

# %%

# Puzzle Input URL
url = 'https://adventofcode.com/2022/day/11/input'

# Get the data 
SESSIONID = open('session_id.txt').read()
USER_AGENT = 'crw873'

# Cache the response if already got 
response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

# %%

# Read the data into an np.array 
raw_input_list = response.text.split('Monkey')[1:]
raw_input_list

# %%

# Read in monkey info 
monkeys = {}
for monkey in raw_input_list:
    monkey_number, starting_items, operation, test, test_true, test_false = monkey.split('\n')[:6]
    monkeys[int(monkey_number[1])] = {
            'Items': starting_items[18:].split(','),
            'Operation': operation[19:],
            'Test Number': int(test.split(' ')[-1]),
            'Next Monkey': [int(test_false.split(' ')[-1]), int(test_true.split(' ')[-1])]
        }

# Set up infrastructure to keep track of number of items a monkey has passed 
monkey_business_counts = {i: 0 for i in range(len(raw_input_list))}

# Get the mod nuber to keep worry levels down 
mod_number = np.prod([monkey['Test Number'] for monkey in monkeys.values()])

# complete twenty rounds of money business  
for round in range(10000):
    print(round)
    for monkey_number, monkey in monkeys.items():
        for item in monkey['Items']:
            # Create old variable for eval statement and execute
            old = int(item)
            item = eval(monkey['Operation'])
            
            # Reduce worry 
            item = np.mod(item, mod_number)

            # Work out next monkey and pass item along
            next_monkey = monkey['Next Monkey'][item % monkey['Test Number'] == 0]
            monkeys[next_monkey]['Items'].append(item)

            # Increment count of how many items this monkey has passed   
            monkey_business_counts[monkey_number] += 1

        # Empty this monkeys items 
        monkey['Items'] = []

monkey_business = np.prod(np.sort(list(monkey_business_counts.values()))[-2:])
monkey_business 
# %%
