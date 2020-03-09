from display import *
from matrix import *

# /*======== void add_circle() ==========
#   Inputs:   struct matrix * edges
#             double cx
#             double cy
#             double r
#             double step
#   Adds the circle at (cx, cy) with radius r to edges
#   ====================*/
def add_circle( points, cx, cy, cz, r, step ):
    full_rot = 2 * math.pi()
    while (theta = full_rot * step <= full_rot):
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        add_point(points, x, y, cz)

# /*======== void add_curve() ==========
# Inputs:   struct matrix *edges
#          double x0
#          double y0
#          double x1
#          double y1
#          double x2
#          double y2
#          double x3
#          double y3
#          double step
#          int type
# Adds the curve bounded by the 4 points passsed as parameters
# of type specified in type (see matrix.h for curve type constants)
# to the matrix edges
# ====================*/
def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    p0 = [x0, y0, z0, 1]
    p1 = [x1, y1, z1, 1]
    p2 = [x2, y2, z2, 1]
    p3 = [x3, y3, z3, 1]
    if (curve_type == 0): #bezier
        coefs = generate_curve_coefs(p0, p1, p2, p3, 0)
    elif (curve_type == 1): #hermite
        coefs = generate_curve_coefs(p0, p1, p2, p3, 1)
    pass

def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print('Need at least 2 points to draw')
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )




def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
