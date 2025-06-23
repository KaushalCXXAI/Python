"""
Exercise Description
    You will write four functions for this exercise. The functions area() and perimeter() have
length and width parameters and the functions volume() and surfaceArea() have length,
width, and height parameters. These functions return the area, perimeter, volume, and surface
area, respectively.
The formulas for calculating area, perimeter, volume, and surface area are based on the length
(L), width (W), and height (H) of the shape:
* area = L x W
* perimeter = L + W + L + W
* volume = L x W x H
* surface area = (L x W x 2) + (L x H x 2) + (W x H x 2)
Area is a two-dimensional measurement from multiplying length and width. Perimeter is the sum
of all of the four one-dimensional lines around the rectangle. Volume is a three-dimensional
measurement from multiplying length, width, and height. Surface area is the sum of all six of the twodimensional areas around the cube. Each of these areas comes from multiplying two of the three
length, width, or height dimensions.

These Python assert statements stop the program if their condition is False. Copy them to
the bottom of your solution program. Your solution is correct if the following assert statements'
conditions are all True:
assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340
"""

def area(L, W):
    return L * W

def perimeter(L, W):
    return 2 * (L + W)

def volume(L, W, H):
    return L * W * H

def surfaceArea(L, W, H):
    return 2 * ((L * W) + (L * H) + (W * H))

assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340