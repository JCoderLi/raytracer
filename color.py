import math

class Color:
    """A three element object used in 3D graphics for rendering color"""
    def __str__(self):
        return "({}, {}, {})".format(self.r, self.g, self.b)

    def __init__(self, r=0.0, g=0.0, b=0.0, maximum=255.0):
        self.r = r
        self.g = g
        self.b = b

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)
    
    def convert(self, mapping=255.0):
        return Color(math.floor(self.r * mapping), math.floor(self.g * mapping), math.floor( self.b * mapping))

    def mult(self, key, value):
        if key == "r":
            return Color(self.r * value, self.g, self.b)
        if key == "g":
            return Color(self.r, self.g * value, self.b)
        if key == "b":
            return Color(self.r, self.g, self.b * value)

    def converttostring(self, mapping=225):
        return "{} {} {}".format(math.floor(self.r * mapping), math.floor(self.g * mapping), math.floor(self.b * mapping))
