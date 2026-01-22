print("advent of code day 6")

global biggest_area
biggest_area = 0

with open('./day7.txt') as f:
    file = f.read().splitlines()

def rectangle_area(point1, point2):
    point1 = point1.split(",")
    point2 = point2.split(",")
    result = 0
    result = abs(int(point2[0])-int(point1[0]) + 1)*abs(int(point2[1])-int(point1[1]) +1)
    # print("area between point:" + str(point1) +" and point: "+ str(point2) + " is equal to " +str(result))
    return result
for point1 in file:
    for point2 in file:
        area = rectangle_area(point1, point2)
        if biggest_area < area:
            biggest_area = area



print("There area of the biggest ractangle is equal to: "+ str(biggest_area))


    