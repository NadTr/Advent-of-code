from pathlib import Path
print("advent of code 2021 day 13")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = f.read().splitlines()

paper_size = [0, 0]
dots = []
folding_instructions = []

def fold(paper, way, line):
    paper_size = [len(paper[0]) if way == 'y' else max(len(paper[0])-line - 1, line), len(paper) if way == 'x' else max(len(paper)-line - 1, line )]
    new_paper = [[ '.' for _ in range(paper_size[0] )] for _ in range(paper_size[1])]
    for i in range(len(new_paper)):
        for j in range(len(new_paper[i])):
            symbol = '#' if paper[i][j] == '#' else '.'
            if way == 'x':
                symbol = '#' if paper[i][-j-1] == '#' else symbol
            else:
                symbol = '#' if paper[-i-1][j] == '#' else symbol
            new_paper[i][j] = symbol
    return new_paper

for line in file : 
    if line == "": continue
    if line[0].isdigit():
        x, y = line.split(',')
        x, y = int(x), int(y)
        if x >= paper_size[0]: paper_size[0] = x + 1
        if y >= paper_size[1]: paper_size[1] = y + 1
        dots.append([x, y])
    else:
        line = line.split()
        instr = line[2].split('=')
        folding_instructions.append([instr[0], int(instr[1])])

paper = [[ '.' for _ in range(paper_size[0])] for _ in range(paper_size[1])]

for dot in dots:
    paper[dot[1]][dot[0]] = '#'

for i in folding_instructions:
    paper = fold(paper, i[0], i[1])

print("The code do you use to activate the infrared thermal imaging camera system is ")

for line in paper:
    print(''.join(c for c in line))