from datetime import datetime
from time import time, sleep
from random import choice
import sys
import webbrowser

intify = lambda element: int(element)
hours, minutes = map(intify, sys.argv[1].split(':'))
links = open('links.txt', 'r').read().split('\n')
date = datetime.now()

isTomorrow = date.hour >= hours and (date.minute >= minutes if date.hour == hours else True)
alarmTime = datetime(
    date.year,
    date.month,
    date.day,
    hours,
    minutes
)
timeDifference = int(abs((date - alarmTime).total_seconds())) + (86400 if isTomorrow else 0)

print(f'Firing alarm in {timeDifference} seconds')
sleep(timeDifference)

link = choice(links)
webbrowser.open(link)