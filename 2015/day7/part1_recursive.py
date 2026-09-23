from pathlib import Path
print("advent of code 2015 day 7")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
    file = [line.split(' -> ') for line in f.read().splitlines()]
   
signals = {}
for l in range(len(file)):
    signals.update({file[l][1]: file[l][0].split()})

def find_wire(wire):
    expr = signals[wire]
    if isinstance(expr, int):
        return expr
    if len(expr) == 1:
        s = int(expr[0]) if expr[0].isdigit() else find_wire(expr[0])

    elif len(expr) == 2 and expr[0] == 'NOT':
        s = 65536 + ~find_wire(expr[1]) 

    elif len(expr) == 3 and (expr[1] == "LSHIFT" or expr[1] == "RSHIFT"):
        s = find_wire(expr[0]) >> int(expr[2]) if expr[1] == "RSHIFT" else find_wire(expr[0]) << int(expr[2])
            
    elif len(expr) == 3:
        s1 = int(expr[0]) if expr[0].isdigit() else find_wire(expr[0])
        s2 = int(expr[2]) if expr[2].isdigit() else find_wire(expr[2])

        if expr[1] == "AND":
            s = s1 & s2 
        elif expr[1] == "OR":
            s = s1 | s2

    signals.update({wire : s})
    return s
        
print("The signal ultimately provided to wire a is ", find_wire('a'))
