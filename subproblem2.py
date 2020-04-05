# create a 3 x 2 pixel image
# FIRST ROW:
# RED = (1,0,0)
# GREEN = (0,1,0)
# BLUE = (0,0,1)
# SECOND ROW
# R+G = (1,1,0)
# R+G+B = (1,1,1)
# R * .001 = (.001,0,0)
# 1 => 225, 0 => 0, map the value between. map()?
# PPM image format:
# P3 [column] [row]
# maximum color value
# RGB triplets

from color import Color

#first row
red = Color(1,0,0)
green = Color(0,1,0)
blue = Color(0,0,1)

#second row
yellow = red + green
white = red + green + blue
special = red.mult("r", .001)

f = open("test.ppm", "w")
f.write("P3 3 2\n")
f.write("255\n")
f.write(" ".join([red.converttostring(), green.converttostring(), blue.converttostring()]))
f.write("\n")
f.write(" ".join([yellow.converttostring(), white.converttostring(), special.converttostring()]))
