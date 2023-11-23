# %%

# General Imports 
import requests
import pandas as pd
from io import StringIO

# %%

# Puzzle Input URL
url = 'https://adventofcode.com/2022/day/7/input'

# Get the data 
SESSIONID = open('session_id.txt').read()
USER_AGENT = 'crw873'

# Cache the response if already got 
response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

# %%

df = pd.read_csv(StringIO(response.text), skip_blank_lines=False, names=['input',])
df
# %%

input_list = response.text.split('\n')
input_list

# %%

class Terminal():
    def __init__(self, input_list):
        self.current_path = '/'
        self.current_directory = '' 
        self.input_list = iter(input_list)
        self.directory_sizes = {'/': 0}
        self.directory_files = {'/': []}
        # self.active_directories = [] # This can be made redundant by pulling from path

    def read_input(self):
        # Get the next instruction from the iterator
        current_instruction = next(self.input_list)
        
        # User the instruction
        if current_instruction[0] == '$':
            self.terminal_command(current_instruction) 
        else:
            self.object_in_directory(current_instruction) 

        # print(current_instruction)
        # print(self.get_active_directories())
        # print(self.directory_sizes)

        return current_instruction

    def terminal_command(self, input):
        # If it isn't changing the directory then we have no action
        if input == '$ ls':
            return None
        
        # Deal with the changing of directory
        elif input[:4] == '$ cd':
            command_indicator, command, target_directory = input.split(' ')
            if target_directory == '/':
                self.current_path= '/'
                self.current_directory = ''
            elif target_directory == '..':
                self.current_path = self.current_path[:-1*(len(self.current_directory)+1)] 
                self.current_directory = self.get_current_directory()
            else:
                self.current_path += target_directory + '/'
                self.current_directory = target_directory

                # In this case we also want to add the directory to the directory sizes dict
                if self.current_directory not in self.directory_sizes:
                    self.directory_sizes[self.current_directory] = 0
                if self.current_directory not in self.directory_files:
                    self.directory_files[self.current_directory] = []

    def object_in_directory(self, input):
        if input[:3] == 'dir':
            return None
        else: 
            file_size, fname = input.split(' ')
            for dir in self.get_active_directories():
                if fname not in self.directory_files[dir]:
                    self.directory_sizes[dir] += int(file_size)
                    self.directory_files[dir].append(fname)

            print(input)
            print(self.current_path)
            print(self.get_active_directories())


    def get_active_directories(self):
        # If base directory return empty list
        active_directories = [dir for dir in self.current_path.split('/') if dir != '']
        # active_directories = self.current_path.split('/')[:-1]
        # active_directories[0] = '/'
        return active_directories 
    
    def get_current_directory(self):
        active_directories = self.get_active_directories()
        if active_directories == []:
            return ''
        else:
            return active_directories[-1]

active_terminal = Terminal(input_list)
for i in range(len(input_list)-1):
    active_terminal.read_input()
    # print(active_terminal.read_input())

# %%

import numpy as np
small_dirs_dict = {dir: file_size for dir, file_size in active_terminal.directory_sizes.items() if file_size <= 100000}
small_dirs_dict
small_dirs = [file_size for file_size in active_terminal.directory_sizes.values() if file_size <= 100000]
np.sum(small_dirs)

# %%

# Stolen Solution
from collections import defaultdict

with open("input.csv") as f:
    commands = f.readlines()

sizes = defaultdict(int)
stack = []

for c in commands:
    if c.startswith("$ ls") or c.startswith("dir"):
        continue
    if c.startswith("$ cd"):
        dest = c.split()[2]
        if dest == "..":
            stack.pop()
        else:
            path = f"{stack[-1]}_{dest}" if stack else dest
            stack.append(path)
    else:
        size, file = c.split()
        for path in stack:
            sizes[path] += int(size)

needed_size = 30000000 - (70000000 - sizes["/"])
for size in sorted(sizes.values()):
    if size > needed_size:
        break

print(sum(n for n in sizes.values() if n <= 100000)) # task 1
print(size) # task 2
# %%
