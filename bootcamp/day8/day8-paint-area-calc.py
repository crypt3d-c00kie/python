#day8
#area calculation
import math

def paint_calc(height,width,coverage):
    res =  (height * width)/5
    res = math.ceil(res) #rounds the number to the highest
    return res

wall_height = int(input("Height of the wall in metre(s) : "))
wall_width = int(input("Width of the wall in metre(s): "))
# wall_height, wall_width = int(input("Enter height and width of the wall : ")).split()
coverage = 5

nCans = paint_calc(wall_height,wall_width,coverage)
#fCan = round(nCans)
print(f"Can(s) required to paint the wall of given area : {nCans}")