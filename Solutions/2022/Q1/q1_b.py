# %%

# General Imports 
import requests
import pandas as pd
from io import StringIO

# %%

# Puzzle Input URL
url = 'https://adventofcode.com/2022/day/1/input'

# Get the data 
SESSIONID = '53616c7465645f5f94f169e4869d1ec9e36e20979d44f0f86c0c2b9d0efeb4bbabc12d9a74347f009381369a06e3f22b34d8fefab3d8b7b21ab5cc76a95b52f2'
USER_AGENT = 'crw873'

# Cache the response if already got 
response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

# %%

# Format the data 
input_data = response.text
data_list = input_data.split('\n')
df = pd.read_csv(StringIO(response.text), skip_blank_lines=False, names=['Calories']).fillna(0)#.astype({'Calories':int})

class MyNumbers:
  def __iter__(self):
    self.current_group = 1
    return self

  def __next__(self):
    x = self.current_group 
    self.current_group  += 1
    return x
    
def set_groups(x, ):
    if x.Calories == 0:
       return next(myiter)
    return myiter.current_group 

myclass = MyNumbers()
myiter = iter(myclass)

df['group'] = df.apply(lambda x: set_groups(x), axis=1)
group_calories = df.groupby('group').sum()
group_calories.sort_values(by='Calories', ascending=False).head(3)

# %%
