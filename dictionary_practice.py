

import csv
from typing import Dict
from pprint import pprint

my_dictionary = { }

"""
keys and values

example:
keys = some country
values = their population
{
    'ghana': 50000
}


Dictionaries

Read the NBA finals CSV data into one more more dictionaries as needed to complete the following:


[x] Write a function that takes as an argument a year and returns the winner of the NBA finals that year.
[x] Write a function that takes as an argument a team name and returns an array of all of the years the team has won the NBA finals.
[x] Which teams have made it to the NBA finals but have never won?
[ ] Print out a ranking of who has won the MVP more than once, by times one, e.g. this output:
    - 6 times: Michael Jordan
    - 3 times: Shaquille O'Neal, LeBron James
    - 2 times: <etc>
"""



def read_csv():
    year_winner = []
    with open('nba_finals.csv', 'r') as file:
        index = 0
        for line in file.readlines():
            if index == 0:
                index += 1
                continue
            items = line.split(',')
            year_winner.append(items[4])
            index += 1

    
    return year_winner


def read_csv_2():
    losers = set()
    with open('nba_finals.csv', 'r') as file:
        index = 0
        for line in file.readlines():
            if index == 0:
                index += 1
                continue
            items = line.split(',')
            losers.add(items[2].strip())
            index += 1
            
    return losers
            

    


year_winner = read_csv()
losers = read_csv_2()
pprint(year_winner)


def winner(year) -> str:
    return year_winner[year]


def mvp_tally():
    mvps = {}
    for winner in year_winner:
        if winner in mvps:
            mvps[winner] += 1
        else:
            mvps[winner] = 1

    for mvp, times_won in mvps.items():
        if times_won > 1:
            print(f"{times_won} times: {mvp}")
    return mvps

mvp_tally()

