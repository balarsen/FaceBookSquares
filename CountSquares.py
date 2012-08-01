# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 09:23:39 2012

@author: balarsen
"""
import itertools
import math

import matplotlib.pyplot as plt
plt.ioff()

class Point(object):
    """
    class to represent a point
    """
    def __init__(self, x, y):
        """
        setup the point with an xy, coord
        """
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __ne__(self, other):
        if self.x == other.x and self.y == other.y:
            return False
        return True

    def dist(self, other):
        tmp = self-other
        return math.sqrt(tmp.x**2 + tmp.y**2)

    def __repr__(self):
        return "Point [{0}, {1}]".format(self.x, self.y)

class Shape(object):
    """
    class that contains 4 points and decides if they are a square
    """
    def __init__(self, a, b, c, d):
        self.Points = [a,b,c,d]

    def __repr__(self):
        return "Shape:\n  {0}\n  {1}\n  {2}\n  {3}".format(*self.Points)

    def isSquare(self):
        """
        return True if the points are a square, False otherwise

        Do this by tallying the distance between points, a square has only 2
        distances, a rectangle has 3 and line has more
        """
        # one special case, very center
        ## python does early bailout
        if Point(1.5, 1.5) in self.Points and \
            Point(2.5, 1.5) in self.Points and \
            Point(1.5, 2.5) in self.Points and \
            Point(2.5, 2.5) in self.Points:
                return False
        collect = set()
        xs = set()
        for aa, bb in itertools.combinations(self.Points, 2):
            tmp = str(aa.dist(bb))
            if aa.x not in xs:
                xs.add(aa.x)
            if bb.x not in xs:
                xs.add(bb.x)
            if tmp not in collect:
                collect.add(tmp)
            if len(collect) > 2 or len(xs) > 2:
                return False
        return True

class Board(list):
    """
    the "game" board to look for squares
    """
    def __init__(self):
        self._squareNum = 0
        x = range(5)
        y = range(5)
        # this is all the points on the board
        pts = list(itertools.product(x, y))
        # add in the inner points
        pts.append((1.5, .5))
        pts.append((1.5, 1.5))
        pts.append((2.5, .5))
        pts.append((2.5, 1.5))
        pts.append((1.5, 2.5))
        pts.append((1.5, 3.5))
        pts.append((2.5, 2.5))
        pts.append((2.5, 3.5))
        for val in pts:
            self.append(Point(*val))

    def countSquares(self):
        for val in itertools.combinations(self, 4):
            tmp = Shape(*val)
            self._squareNum += tmp.isSquare()
            if tmp.isSquare():
                ax = self.plot()
                self.plotSquare(ax, tmp)
        print self._squareNum

    def plotSquare(self, ax, shape):
        for v1, v2 in itertools.permutations(shape.Points, 2):
            #            ax.plot([shape.Points[0].x, shape.Points[1].x], [shape.Points[0].y, shape.Points[1].y], 'r', lw=3)
            ax.plot([v1.x, v2.x], [v1.y, v2.y], 'r', lw=2)
        # ax.set_title('Square Number: {0}'.format(self._squareNum))
        ax.text(4, 4, str(self._squareNum), fontsize=50, color='r')
        plt.savefig('{0:03}.png'.format(self._squareNum))
        plt.close()

    def plot(self):
        fig = plt.figure(figsize=(8,8))
        ax = fig.add_subplot(111, aspect='equal')
        for val in self:
            ax.plot(val.x, val.y, 'bo')
        ax.set_xlim([-1,5])
        ax.set_ylim([-1,5])

        x = range(5)
        y = range(5)
        # vert lines
        for xx in x:
            ax.plot([xx]*2, [0,4], 'g', lw=1)
        # horiz lines
        for yy in y:
            ax.plot([0,4], [yy]*2, 'g', lw=1)
        # inner boxes
        ax.plot([1.5]*2, [.5, 1.5], 'g', lw=1)
        ax.plot([2.5]*2, [.5, 1.5], 'g', lw=1)
        ax.plot([1.5]*2, [2.5, 3.5], 'g', lw=1)
        ax.plot([2.5]*2, [2.5, 3.5], 'g', lw=1)
        ax.plot([1.5, 2.5], [0.5]*2, 'g', lw=1)
        ax.plot([1.5, 2.5], [1.5]*2, 'g', lw=1)
        ax.plot([1.5, 2.5], [2.5]*2, 'g', lw=1)
        ax.plot([1.5, 2.5], [3.5]*2, 'g', lw=1)

        return ax

if __name__ == '__main__':
    B = Board()
    B.countSquares()




