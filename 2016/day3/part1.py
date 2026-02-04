print("advent of code 2016 day 3")

with open('./input.txt') as f:
    file = f.read().splitlines()

number_of_possible_triangles = 0

def is_triangle_possible(triangle):
    c1 = int(triangle[0])        
    c2 = int(triangle[1])        
    c3 = int(triangle[2])
    if c1 + c2 > c3 and    c3 + c1 > c2 and  c2 + c3 > c1:
        return True
    else:
        return False 
    
step = 0
triangle1 = [0,0,0]
triangle2 = [0,0,0]
triangle3 = [0,0,0]

for line in file:
    vars = line.split()
    triangle1[step] = vars[0]
    triangle2[step] = vars[1]
    triangle3[step] = vars[2]

    if step < 2:
        step += 1
    else:
        # print(triangle1, triangle2, triangle3)
        if(is_triangle_possible(triangle1)):
            number_of_possible_triangles += 1
        if(is_triangle_possible(triangle2)):
            number_of_possible_triangles += 1
        if(is_triangle_possible(triangle3)):
            number_of_possible_triangles += 1
        step = 0

print("The number of possible triangles is ", number_of_possible_triangles)