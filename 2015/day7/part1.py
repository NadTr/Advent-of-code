from pathlib import Path
print("advent of code 2015 day 7")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = [line.split(' -> ') for line in f.read().splitlines()]
    for l in range(len(file)):
        file[l][0] = file[l][0].split()
   
signals = {}

while 'a' not in signals.keys():
    for line in file:
        if line[1] in signals.keys(): continue

        if len(line[0]) == 1:
            if line[0][0].isdigit() or line[0][0] in signals.keys():
                s = int(line[0][0]) if line[0][0].isdigit() else signals[line[0][0]]
                signals.update({line[1] : s})

        elif len(line[0]) == 2 and line[0][0] == 'NOT':
            if line[0][1] in signals.keys():
                signals.update({line[1] : 65536 + ~signals[line[0][1]] })

        elif len(line[0]) == 3 and (line[0][1] == "LSHIFT" or line[0][1] == "RSHIFT"):
            if line[0][0] in signals.keys():
                s = signals[line[0][0]] >> int(line[0][2]) if line[0][1] == "RSHIFT" else signals[line[0][0]] << int(line[0][2])
                signals.update({line[1] : s})
                
        elif len(line[0]) == 3:
            if (line[0][0] in signals.keys() or line[0][0].isdigit()) and (line[0][2] in signals.keys() or line[0][2].isdigit()):
                s1 = int(line[0][0]) if line[0][0].isdigit() else signals[line[0][0]]
                s2 = int(line[0][2]) if line[0][2].isdigit() else signals[line[0][2]]

                if line[0][1] == "AND":
                    signals.update({line[1] : s1 & s2 })
                elif line[0][1] == "OR":
                    signals.update({line[1] : s1 | s2 })
        
print("The signal ultimately provided to wire a is ", signals['a'])
