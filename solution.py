#!/usr/bin/python

import sys, os.path

# Import classes.
from file import File
from asteroid_group import AsteroidGroup

# Check for presence of a filename argument and existence of the file.
if len(sys.argv) < 2:
    sys.stderr.write("Error: No filename. This script must be executed with a valid filename argument.\n")
    sys.exit(1)
if not os.path.isfile(sys.argv[1]):
    sys.stderr.write("Error: File does not exist.\n")
    sys.exit(1)

# Validate and import data from the file.
file = File(sys.argv[1])

# Create all the asteroids from the file.
asteroids = []
for coordinates in file.lines_as_coordinates:
    asteroids.append([coordinates[0], coordinates[1]])

# Create an object with our list of asteroids.
asteroid_group = AsteroidGroup(asteroids)

# Find asteroid with narrowest angle of view relative to the others and prints its coordinates to standard out.
asteroid_group.choose_asteroid()
