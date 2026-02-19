from pathlib import Path
from collections import Counter, OrderedDict
from datetime import date, datetime, timedelta
# import numpy as np, re
print("advent of code 2018 day 4")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     file = f.read().splitlines()

file = sorted(file)
guards_shifts = {}
guards_time_asleep = {}

def find_safest_minute(guard):
    safest_minute = 0
    all_minutes_asleep = []
    for shift in guards_shifts[guard]:
        all_minutes_asleep += guards_shifts[guard][shift]["sleeping_time"]   
    days_asleep_at_that_minute = Counter(all_minutes_asleep)
    days_asleep_at_that_minute = OrderedDict(reversed(sorted(days_asleep_at_that_minute.items())))
    safest_minute = max(days_asleep_at_that_minute, key=days_asleep_at_that_minute.get) 
    return safest_minute

for line in file:
    line = line.split("]")
    day_date, time = line[0][1:].split()
    actions = line[1].split()
    if actions[0] == "Guard":
        if "guard_id" in locals():
            time_asleep = len(sleeping_minutes)
            if guard_id in guards_shifts:
                guards_shifts[guard_id].update({day_date:{ "sleeping_time":sleeping_minutes, "time_asleep":time_asleep}})
                guards_time_asleep[guard_id] += time_asleep
            else:
                guards_shifts.update({guard_id:{day_date:{ "sleeping_time":sleeping_minutes, "time_asleep":time_asleep}}})
                guards_time_asleep.update({guard_id:time_asleep})
        guard_id = actions[1]
        if time[0] == "0":
            day_date = datetime.strptime(day_date, '%Y-%m-%d').date()  
        else: 
            day_date = datetime.strptime(day_date, '%Y-%m-%d').date() + timedelta(days=1)
        sleeping_minutes = []
    elif actions[0] == "falls":
        if len(sleeping_minutes)%2 == 0:
            sleeping_minutes += [int(time[-2:])]
    else:
        if len(sleeping_minutes)%2 == 1:
            sleeping_minutes+= range(sleeping_minutes[-1] + 1 ,int(time[-2:]))
    
guard_most_asleep = max(guards_time_asleep, key=guards_time_asleep.get)
safest_minute = find_safest_minute(guard_most_asleep)

result = int(guard_most_asleep[1:]) * safest_minute

print("The ID of the guard you chose multiplied by the minute where they're the most asleep is", result)