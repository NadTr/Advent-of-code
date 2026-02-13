from pathlib import Path
print("advent of code 2016 day 3")

script_location = Path(__file__).absolute().parent
with open(script_location /'input.txt') as f:
     file = f.read().splitlines()

number_of_possible_triangle = 0

def is_triangle_possible(triangle):
    c1 = int(triangle[0])        
    c2 = int(triangle[1])        
    c3 = int(triangle[2])
    if c1 + c2 > c3 and    c3 + c1 > c2 and  c2 + c3 > c1:
        return True
    else:
        return False 
    

for line in file:
    triangle = line.split()
    if(is_triangle_possible(triangle)):
        number_of_possible_triangle += 1

print("The number of possible traingles is ", number_of_possible_triangle)