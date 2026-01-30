print("advent of code 2015 day 2")

with open('./input.txt') as f:
    file = f.read().splitlines()

result = 0

def wrapping_paper_needed(l, w, h):
    smallest_addon = min(l*w, w*h, h*l)
    exact_surface = 2*l*w + 2*w*h + 2*h*l
    # print("smallest_addon ", smallest_addon, " exact surface ", exact_surface)
    return exact_surface + smallest_addon

for line in file:
    line = line.split("x")
    result += wrapping_paper_needed(int(line[0]), int(line[1]), int(line[2]))
    
print("The number of square needed to wrap presents is ", result)