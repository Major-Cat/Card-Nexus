def bilinear_interpolation(x, y, points):  
    #effectivley a 3D line of best fit using 4 points
    #compared to results found online this seems functional
    points = sorted(points)               # order points by x, then by y
    (x1, y1, z1), (_x1, y2, z2), (x2, _y1, z3), (_x2, _y2, z4) = points #generates each of the coordinates for the four points being measured between

    if x1 != _x1 or x2 != _x2 or y1 != _y1 or y2 != _y2:    #confirms the points make a rectangle to interpolate between
        raise ValueError('points do not form a rectangle')
    if not x1 <= x <= x2 or not y1 <= y <= y2:  #confirms point being searched for is within the confines of the rectangle
        raise ValueError('(x, y) not within the rectangle')

    ans = (z1 * (x2 - x) * (y2 - y) + z3 * (x - x1) * (y2 - y) + z2 * (x2 - x) * (y - y1) + z4 * (x - x1) * (y - y1)) / ((x2 - x1) * (y2 - y1) + 0.0)
    #pretty certain this works
    return ans

#draws = 43  #number of times a set of cards has been drawn
#wins = 40    #number of times a set of cards has won in epochs
#win_ratio = (wins/draws) * 100  #percentage chance of the current hand of winning
#print("wins = "+str(draws*(win_ratio/100)))

# EXAMPLE USE:
#print(bilinear_interpolation(draws,win_ratio,[(1,0,20.0),(1,100,100.0),(217,0,0.1),(217,100,100.0)]))   #   x = times drawn, y = win/lose ratio (percent), z = chance of play

#[(1,0,20),(1,100,100),(200,0,0),(200,100,100)] is the dataset
#(1,0,20) = 1 draw, 0 wins, 20% chance
#(1,100,100) = 1 draw, 1 win, 100% chance
#(217,0,0) = 217 draw, 0 win, 0.1% chane
#(217,100,100) = 217 draw, 200 win, 100% chance