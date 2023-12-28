#initialise global variables
colours=["red","green","blue"]
var_red=0
var_green=1
var_blue=2
content=[12,13,14]

#returns game no from input line
def game_no(line:str)->int:
    game = int(line.split(":")[0].split()[1])
    return game

#returns the min number of cubes of each colour (r/g/b) in bag to allow extraction 
def min_cubes(line:str)->list[int]:
    bags = line.split(":")[1].split(";")
    cube_min=[0,0,0]
    for bag in bags:
        cubes=bag.split(",")
        for cube in cubes:
            cube_attr=cube.split()
            cube_colour=cube_attr[1]
            cube_no = int(cube_attr[0])
            if  cube_colour=='red' and cube_no>cube_min[var_red]:
                cube_min[var_red]=cube_no
            elif cube_colour=='green' and cube_no>cube_min[var_green]:
                cube_min[var_green]=cube_no
            elif cube_colour=='blue' and cube_no>cube_min[var_blue]:
                cube_min[var_blue]=cube_no
    return cube_min

#checks whether all items in 1st list less than/equal to equiv items in 2nd list
def compare_lists(smaller:list[int], bigger:list[int])->bool:
    if smaller and len(smaller) != len(bigger):
        return False
    else:
        for item in range(len(smaller)):
            if smaller[item]>bigger[item]:
                return False
        return True

#Day2 part 1
with open("input_day2.txt", "r") as data_file:
    lines = data_file.readlines()
sum_lines = 0
for line in lines:
    if compare_lists(min_cubes(line), content):
        sum_lines += game_no(line)
print(sum_lines)

#Day2 part 2
sum_power_lines=0
for line in lines:
    cube_power=1
    for cube in min_cubes(line):
        cube_power *= cube
    sum_power_lines += cube_power
print(sum_power_lines)

