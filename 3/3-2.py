import os, sys


dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

## creating these variables as sets to remove dupes upon addition
squares_used = set()
squares_doubled = set()

##loop through input rows, or "rectangles"
with open(os.path.join(dirname, "input.txt")) as rectangle_list:
    rectangles = [rectangles.split() for rectangles in rectangle_list]

for rectangle in rectangles:
    ##parse the rectangle data into x, y, width, and height
    xy = rectangle[2].split(",")
    x = int(xy[0])
    y = int(xy[1][:-1])

    wh = rectangle[3].split("x")
    width = int(wh[0])
    height = int(wh[1])

    ##loop through all squares in rectangle
    for i in range(width):
        for j in range(height):
            square = (i + x, j + y)

            ##if a coordinate is already in the list, add to squares_doubled
            if (square in squares_used):
                squares_doubled.add(square)

            ##add to squares_used
            squares_used.add(square)

for rectangle in rectangles:
    ##parse the rectangle data into x, y, width, and height BUT this time also save the id (rid)
    rid = rectangle[0]
    unique = True

    xy = rectangle[2].split(",")
    x = int(xy[0])
    y = int(xy[1][:-1])

    wh = rectangle[3].split("x")
    width = int(wh[0])
    height = int(wh[1])

    ##loop through again, this time testing if any are in squares_doubled
    for i in range(width):
        for j in range(height):
            square = (i + x, j + y)

            ##if a coordinate is in squares_doubled, it is not unique
            if (square in squares_doubled):
                unique = False

    if unique:
        print(rid)
            