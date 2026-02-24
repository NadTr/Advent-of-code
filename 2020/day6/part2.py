from pathlib import Path
import re
print("advent of code 2020 day 6")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().split("\n\n")

total_positive_answers = 0

for line in file:
    answers = set(re.findall(r"[a-z]", line))
    line = line.splitlines()
    for person in line:
        person = set(re.findall(r"[a-z]", person))

        negative = answers - person
        for n in negative:
            answers.discard(n)

    total_positive_answers += len(answers)

print("The number of questions to which everyone answered \"yes\" is", total_positive_answers)