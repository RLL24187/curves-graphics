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
    full_rot = 2 * math.pi
    t = 0
    x0 = r * math.cos(0) + cx
    y0 = r * math.sin(0) + cy
    while (t < 1):
        t += step
        theta = full_rot * t
        x1 = r * math.cos(theta) + cx
        y1 = r * math.sin(theta) + cy
        add_edge(points, x0, y0, cz, x1, y1, cz)
        x0 = x1
        y0 = y1

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
    x_coefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)
    y_coefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)
    # print_matrix(x_coefs)
    # print_matrix(y_coefs)
    first_x = x0
    first_y = y0
    t = 0
    while (t < 1):
        t += step
        t2 = t * t
        t3 = t2 * t
        second_x = x_coefs[0][0] * t3 + x_coefs[0][1] * t2 + x_coefs[0][2] * t + x_coefs[0][3]
        second_y = y_coefs[0][0] * t3 + y_coefs[0][1] * t2 + y_coefs[0][2] * t + y_coefs[0][3]
        add_edge(points, first_x, first_y, 0, second_x ,second_y, 0)
        first_x = second_x
        first_y = second_y


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
