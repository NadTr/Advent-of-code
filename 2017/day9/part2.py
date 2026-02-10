import re
print("advent of code 2017 day 9")
with open('./input.txt') as f:
    file = f.read()

file = re.sub(r'\!.{1}', '', file)
results = re.findall(r'<.*?>', file)

# print(results)


score = 0
for r in results:
    score += len(r) -2

print("The total garbage length for all groups is", score)