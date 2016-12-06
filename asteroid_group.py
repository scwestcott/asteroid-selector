#!/usr/bin/python

class AsteroidGroup(object):
    """Creates a group of asteroids from which to compare angles of view and 
    choose the one with the narrowest angle of view as the best one to land on.

    Attributes:
        asteroids: a list of the asteroids for consideration.
        asteroid_convex_hull: a list that will contain the points thay lie on the convex hull of our heap of asteroids.
    """

    asteroids = []
    asteroid_convex_hull = []

    def __init__(self, asteroids):
        """Initialize our asteroid group with a list of asteroids."""
        self.asteroids = asteroids
        self.asteroid_convex_hull = self.convex_hull()

    def turn(self, p, q, r):
        """Determines turn direction of a 3rd point relative to the first two points.
        Borrowed from http://tomswitzer.net/2010/03/graham-scan/"""
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _keep_left(self, hull, r):
        """If the turn is right or straight, discard the middle point. Repeat.
        Borrowed from http://tomswitzer.net/2010/03/graham-scan/"""
        while len(hull) > 1 and self.turn(hull[-2], hull[-1], r) != 1:
            hull.pop()
        hull.append(r)
        return hull

    def convex_hull(self):
        """Returns points on convex hull of an array of points in CCW order.
        Borrowed from http://tomswitzer.net/2010/03/graham-scan/"""

        points = sorted(self.asteroids)
        l = reduce(self._keep_left, points, [])
        u = reduce(self._keep_left, reversed(points), [])
        # We don't include the first or last point when extending l.
        l.extend(u[i] for i in xrange(1, len(u) - 1))
        return l

    # Update method to iterate around the heapsort to find the asteroid with narrowest viewing angle
    def choose_asteroid(self):
        """Find viewing angles for all asteroids and then choose the one with the narrowest"""

        hull_asteroids_by_view_angle = {}
        hull_size = len(self.asteroid_convex_hull)

        # The convex hull has all the asteroids on the perimiter of the asteroid field, in order.
        # Now we need to go to each asteroid and determine its angle of view by calculating the angle 
        # of view between the previous and next asteroids.
        for i in range(0, hull_size):
            p0 = self.asteroid_convex_hull[i - 1]
            p1 = self.asteroid_convex_hull[i]

            # If we're at the end of the array, p2 is the first asteroid in the array.
            if i == hull_size - 1:
                p2 = self.asteroid_convex_hull[0]
            else:
                p2 = self.asteroid_convex_hull[i + 1]

            # Now that we have the three points, find the angle of view.
            angle_of_view = self.find_angle(p0, p1, p2)

            # Store the current asteroid in our dictionary, with the angle of view as the index.
            hull_asteroids_by_view_angle[angle_of_view] = self.asteroid_convex_hull[i]

        # Find and select the asteroid that had the narrowest angle of view.
        lowest_angle_key = min(hull_asteroids_by_view_angle)
        chosen_asteroid = hull_asteroids_by_view_angle[lowest_angle_key]

        # For whole number floats, convert them to integers before printing.
        chosen_asteroid = self.whole_floats_to_ints(chosen_asteroid)

        # Print x, y coordinates of chosen asteroid to standard out.
        print chosen_asteroid[0], chosen_asteroid[1]

    def find_angle(self, p0, p1, p2):
        """Given three points, find the angle of view.
        Adapted from: http://jsfiddle.net/d3aZD/88/"""
        import math

        p0p1 = math.pow(p1[0] - p0[0], 2) + math.pow(p1[1] - p0[1], 2)
        p2p1 = math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2)
        p0p2 = math.pow(p2[0] - p0[0], 2) + math.pow(p2[1] - p0[1], 2)
        return math.acos( (p2p1 + p0p1 - p0p2) / math.sqrt(4 * p2p1 * p0p1) ) * 180 / math.pi

    def whole_floats_to_ints(self, asteroid):
        """Convert whole-number floats to integers to drop the '.0' before printing."""
        import math

        if asteroid[0] == math.floor(asteroid[0]):
            asteroid[0] = int(asteroid[0])
        if asteroid[1] == math.floor(asteroid[1]):
            asteroid[1] = int(asteroid[1])

        return asteroid

