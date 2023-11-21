# %%

# General Imports 
import requests
import pandas as pd
from io import StringIO

# %%

# Puzzle Input URL
url = 'https://adventofcode.com/2022/day/3/input'

# Get the data 
SESSIONID = open('session_id.txt').read()
USER_AGENT = 'crw873'

# Cache the response if already got 
response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

# %%

# Format the data 
df = pd.read_csv(StringIO(response.text), skip_blank_lines=False, names=['items']).fillna(0)#.astype({'Calories':int})

char_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
score_lookup_dict = {c:n for c,n in zip(char_str, range(1, 53))}

df['Group'] = [i // 3 for i in range(df.shape[0])]
group_df = df.groupby('Group').agg(lambda x: list(x))

# %%

def get_score(x):
    init_elf = set(x[0])
    for elf in x[1:]:
        init_elf = init_elf.intersection(set(elf))
    return score_lookup_dict[min(init_elf)]

group_df['Score'] = group_df['items'].apply(lambda x: get_score(x))
group_df.sum()

# %%
