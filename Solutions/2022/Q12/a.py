# %%

# General Imports 
import requests
import pandas as pd
from io import StringIO
import numpy as np

# %%

# Puzzle Input URL
url = 'https://adventofcode.com/2022/day/12/input'

# Get the data 
SESSIONID = open('session_id.txt').read()
USER_AGENT = 'crw873'

# Cache the response if already got 
response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

# %%

# Read the data into an np.array 
raw_input_list = response.text.split('\n')[:-1]
input_array = np.array([list(row) for row in raw_input_list])

# %%

# STOLEN from https://github.com/nthistle/advent-of-code/blob/master/2022/day12/day12.py

import string
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

s = response.text.strip()

g = [list(x) for x in s.split("\n")]
n = len(g)
m = len(g[0])

sx,sy = [(i,j) for i in range(n) for j in range(m) if g[i][j] == "S"][0]
tx,ty = [(i,j) for i in range(n) for j in range(m) if g[i][j] == "E"][0]

g[sx][sy] = "a"
g[tx][ty] = "z"

g = [[ord(c) - ord("a") for c in r] for r in g]

from collections import deque, defaultdict, Counter

dst = defaultdict(lambda : 1000000)

part = 2
# part 1:
if part == 1:
    q = deque([(sx,sy)])
else:
    q = deque([(i,j) for i in range(n) for j in range(m) if g[i][j] == 0])
    
for x,y in q:
    dst[x,y] = 0
    
ans = 100000
while len(q) > 0:
    cx,cy = q.popleft()
    if (cx,cy) == (tx,ty):
        ans = dst[tx,ty]
        print(ans)
        break
    for dx,dy in dirs:
        nx,ny = cx+dx,cy+dy
        if nx in range(n) and ny in range(m):
            if g[cx][cy] >= g[nx][ny] - 1:
                ndst = dst[cx,cy] + 1
                if ndst < dst[nx,ny]:
                    q.append((nx,ny))
                    dst[nx,ny] = ndst


# %%
