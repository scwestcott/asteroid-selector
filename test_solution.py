#!/usr/bin/python

import os

# Format and run each test.
def run_test(filename, should_get):
    command = "python solution.py "
    if filename != None:
        command += "test_input_files/" + filename
    print "\nShould get vs. got:\n%s" % should_get
    os.system(command)

# Send filename and expected output to the run_test function for each test.
run_test(None, "Error: No filename. This script must be executed with a valid filename argument.")
run_test("bad_file.txt", "Error: File does not exist.")
run_test("shouldErrorIfAsteroidCountIsNonInteger.txt", "Error: Expected asteroid count is a non-integer: 8d")
run_test("shouldErrorIfAsteroidCountMismatches.txt", "Error: Expected 5 asteroids but got 3.")
run_test("shouldErrorIfAsteroidHasMoreThanTwoCoordinates.txt", "Error: 3 coordinates in asteroid 1 1. Expected exactly 2.")
run_test("shouldErrorIfCoordinatesContainNonFloats.txt", "Error: An asteroid contains a non-numeric coordinate: 0 0d")
run_test("shouldErrorIfFewerThanThreeAsteroids.txt", "Error: There are only 2 asteroids. There must be at least 3.")
run_test("shouldErrorIfMissingAsteroidCount.txt", "Error: Expected asteroid count is a non-integer: 10 10")
run_test("shouldErrorIfFileIsEmpty.txt", "Error: File does not contain any data.")
run_test("shouldErrorIfTwoAsteroidsExistAtSameLocation.txt", "Error: Two asteroids found at 0 0. Only one asteroid may exist per location.")
run_test("shouldPick_0_0.txt", "0 0")
run_test("shouldPick_-100_50.txt", "-100 50")
run_test("shouldPick_10_0.txt", "10 0")
run_test("shouldPick_5.23_10.99.txt", "5.23 10.99")
run_test("shouldPick_52_-63.txt", "52 -63")
run_test("shouldPick_2000_2000.txt", "2000 2000")
run_test("shouldPick_2001_2000.txt", "2001 2000")
