# I want this python script to be able to generate ascii art
# of ellipses based on command line parameters.

from math import *
from convex_polygon import *

class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        v = [(x, y), (x+1., y), (x+1., y+1.), (x, y+1.)]
        self.poly = ConvexPolygon(v)

    def trim_outer(self, p0, p1):
        assert(type(p0) == tuple)
        assert(len(p0) >= 2)
        assert(type(p1) == tuple)
        assert(len(p1) >= 2)
        tri = ConvexPolygon([(0., 0.), p0, p1])
        # Ignore double solutions. We can only get away with
        # this because we're using unit thickness ellipses.
        eps = 0.00001
        a = tri.area()
        if abs(a) < eps:
            return
        elif a < 0: # Reorder if necessary.
            temp = p1
            p1 = p0
            p0 = temp
        self.poly.trim(p0, p1)

    # Inner ellipse vertex ordering is clockwise.
    def trim_inner(self, p0, p1):
        assert(type(p0) == tuple)
        assert(len(p0) >= 2)
        assert(type(p1) == tuple)
        assert(len(p1) >= 2)
        tri = ConvexPolygon([(0., 0.), p0, p1])
        # Ignore double solutions. We can only get away with
        # this because we're using unit thickness ellipses.
        eps = 0.00001
        a = tri.area()
        if abs(a) < eps:
            return
        elif a > 0: # Reorder if necessary.
            temp = p1
            p1 = p0
            p0 = temp
        self.poly.trim(p0, p1)

class Ellipse(object):
    def __init__(self, a, b, th):
        self.a = float(a)
        self.b = float(b)
        self.th = float(th)
        c = cos(th)
        s = sin(th)
        self.A = (c*c)/(a*a) + (s*s)/(b*b)
        self.B = 2*c*s*(1.0/(a*a) - 1.0/(b*b))
        self.C = (s*s)/(a*a) + (c*c)/(b*b)

    def solve_y(self, x):
        A = self.A
        B = self.B
        C = self.C
        det = -4*A*C*x*x + B*B*x*x + 4*C
        if det >= 0:
            r = sqrt(det)
            return ((r-B*x)/(2*C), (-r-B*x)/(2*C))
        else:
            return None

    def solve_x(self, y):
        A = self.A
        B = self.B
        C = self.C
        det = -4*A*C*y*y + B*B*y*y + 4*A
        if det >= 0:
            r = sqrt(det)
            return ((r-B*y)/(2*A), (-r-B*y)/(2*A))
        else:
            return None

def ellipse(x, y, th, a, b):
    X = x * cos(th) + y * sin(th)
    Y = x * sin(th) - y * cos(th)
    return (X*X) / (a*a) + (Y*Y) / (b*b)


def ellipse_points(e):
    assert(type(e) == Ellipse)
    p = []
    x = 0.
    seeking = True
    while seeking:
        y_pair = e.solve_y(x)
        if y_pair:
            p.append((x, y_pair[0]))
            p.append((x, y_pair[1]))
        else:
            seeking = False
        x += 1.

    seeking = True
    x = -1.
    while seeking:
        y_pair = e.solve_y(x)
        if y_pair:
            p.append((x, y_pair[0]))
            p.append((x, y_pair[1]))
        else:
            seeking = False
        x -= 1.

    seeking = True
    y = 0.
    while seeking:
        x_pair = e.solve_x(y)
        if x_pair:
            p.append((x_pair[0], y))
            p.append((x_pair[1], y))
        else:
            seeking = False
        y += 1.

    seeking = True
    y = -1.
    while seeking:
        x_pair = e.solve_x(y)
        if x_pair:
            p.append((x_pair[0], y))
            p.append((x_pair[1], y))
        else:
            seeking = False
        y -= 1.

    return p

def raster_ellipse(a, b, th):
    assert(a > 1. and b > 1.)
    min_x = None
    max_x = None
    min_y = None
    max_y = None
    outer = Ellipse(a, b, th)
    inner = Ellipse(a-1., b-1., th)
    
    outer_points = ellipse_points(outer)
    inner_points = ellipse_points(inner)
    both = inner_points + outer_points

    # Now create a sparse array of pixels from the lists.
    # For now I'm going to re-solve. I know it's inefficient, so
    # that will be something to optimize.
    pixels = {}
    for point in both:
        (x, y) = (floor(point[0]), floor(point[1]))
        if not min_x:
            min_x = x
            max_x = x
            min_y = y
            max_y = y
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y

        if not (x, y) in pixels:
            p = Pixel(x, y)
            points = []
            # Lower edge
            x_pair = outer.solve_x(y)
            if x_pair:
                (x0, x1) = x_pair
                if x0 >= x and x0 <= x+1:
                    points.append((x0, y))
                if x1 >= x and x1 <= x+1:
                    points.append((x1, y))
            # Right edge
            y_pair = outer.solve_y(x+1.)
            if y_pair:
                (y0, y1) = y_pair
                if y0 >= y and y0 <= y+1:
                    points.append((x+1., y0))
                if y1 >= y and y1 <= y+1:
                    points.append((x+1., y1))
            # Upper edge
            x_pair = outer.solve_x(y+1.)
            if x_pair:
                (x0, x1) = x_pair
                if x0 >= x and x0 <= x+1:
                    points.append((x0, y+1.))
                if x1 >= x and x1 <= x+1:
                    points.append((x1, y+1.))
            # Left edge
            y_pair = outer.solve_y(x)
            if y_pair:
                (y0, y1) = y_pair
                if y0 >= y and y0 <= y+1:
                    points.append((x, y0))
                if y1 >= y and y1 <= y+1:
                    points.append((x, y1))

            if (len(points) >= 2):
                # To be honest, it's a huge pain to account for
                # situtations other than a pair, and it will not 
                # likely make a huge difference.
                p.trim_outer(points[0], points[1])

            # Repeat for inner vertices.
            points = []
            # Lower edge
            x_pair = inner.solve_x(y)
            if x_pair:
                (x0, x1) = x_pair
                if x0 >= x and x0 <= x+1:
                    points.append((x0, y))
                if x1 >= x and x1 <= x+1:
                    points.append((x1, y))
            # Right edge
            y_pair = inner.solve_y(x+1.)
            if y_pair:
                (y0, y1) = y_pair
                if y0 >= y and y0 <= y+1:
                    points.append((x+1., y0))
                if y1 >= y and y1 <= y+1:
                    points.append((x+1., y1))
            # Upper edge
            x_pair = inner.solve_x(y+1.)
            if x_pair:
                (x0, x1) = x_pair
                if x0 >= x and x0 <= x+1:
                    points.append((x0, y+1.))
                if x1 >= x and x1 <= x+1:
                    points.append((x1, y+1.))
            # Left edge
            y_pair = inner.solve_y(x)
            if y_pair:
                (y0, y1) = y_pair
                if y0 >= y and y0 <= y+1:
                    points.append((x, y0))
                if y1 >= y and y1 <= y+1:
                    points.append((x, y1))

            if (len(points) >= 2):
                # To be honest, it's a huge pain to account for
                # situtations other than a pair, and it will not 
                # likely make a huge difference.
                p.trim_inner(points[0], points[1])

            pixels[(x, y)] = p
        # endif
    #end for
    return [[(min_x, min_y), (max_x, max_y)], pixels]

def render_raster(raster):
    [(min_x, min_y), (max_x, max_y)] = raster[0]
    pixels = raster[1]
    s = ''
    y = max_y
    while y >= min_y:
        x = min_x
        while x <= max_x:
            if (x, y) in pixels:
                p = pixels[(x, y)]
                a = p.poly.area()
                if a < 0.25:
                    s += ' '
                elif a < 0.625:
                    s += '.'
                elif a < 0.875:
                    s += 'o'
                else:
                    s += 'O'
            else:
                s += ' '
            x+=1.0
        y -= 1.0
        s+='\n'
    return s
