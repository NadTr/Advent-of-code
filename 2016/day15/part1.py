from pathlib import Path
print("advent of code 2016 day 15")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

def get_disc_position(disc, time):
    position_at_a_time = (discs[disc]["start_position"] + time)% discs[disc]["number_of_positions"]
    return position_at_a_time

discs = {}
disc_not_ok = True
time = 0

for line in file:
    (disc, info) = line.split( " has ")
    (number_of_positions, start_position) = info.split(" positions; at time=0, it is at position ")
    discs.update({disc :{"number_of_positions":int(number_of_positions), "start_position" : int(start_position[:-1])}})

while disc_not_ok:
    delay = 1
    positions = []
    for disc in discs:
        positions += [get_disc_position(disc, time + delay)]
        delay += 1
    if sum(positions) == 0:
        disc_not_ok = False
    else:
        time += 1

print("The index first time you can press the button to get a capsule is", time)