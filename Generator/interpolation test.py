def bilinear_interpolation(x, y, points):
    '''Interpolate (x,y) from values associated with four points.
    The four points are a list of four triplets:  (x, y, value).
    The four points can be in any order.  They should form a rectangle.

        >>> bilinear_interpolation(12, 5.5,
        ...                        [(10, 4, 100),
        ...                         (20, 4, 200),
        ...                         (10, 6, 150),
        ...                         (20, 6, 300)])
        165.0

    '''
    # See formula at:  http://en.wikipedia.org/wiki/Bilinear_interpolation

    points = sorted(points)               # order points by x, then by y
    (x1, y1, q11), (_x1, y2, q12), (x2, _y1, q21), (_x2, _y2, q22) = points

    if x1 != _x1 or x2 != _x2 or y1 != _y1 or y2 != _y2:
        raise ValueError('points do not form a rectangle')
    if not x1 <= x <= x2 or not y1 <= y <= y2:
        raise ValueError('(x, y) not within the rectangle')

    return (q11 * (x2 - x) * (y2 - y) + q21 * (x - x1) * (y2 - y) + q12 * (x2 - x) * (y - y1) + q22 * (x - x1) * (y - y1)) / ((x2 - x1) * (y2 - y1) + 0.0)

draws = 43  #number of times a set of cards has been drawn
wins = 40    #number of times a set of cards has won in epochs
win_ratio = (wins/draws) * 100  #percentage chance of the current hand of winning
#print("wins = "+str(draws*(win_ratio/100)))

print(bilinear_interpolation(draws,win_ratio,[(1,0,20.0),(1,100,100.0),(217,0,0.1),(217,100,100.0)]))   #   x = times drawn, y = win/lose ratio (percent), q = chance of play
#[(1,0,20),(1,100,100),(200,0,0),(200,100,100)] is the dataset
#(1,0,20) = 1 draw, 0 wins, 20% chance
#(1,100,100) = 1 draw, 1 win, 100% chance
#(200,0,0) = 200 draw, 0 win, 0.1% chane
#(200,100,100) = 200 draw, 200 win, 100% chance