# Asteroid Selector

## Purpose

We're exploring a group of asteroids that are well behaved in that they all move in the same  
plane and are static to one another. A space craft, equipped with measuring devices, will land  
on one of the asteroids to perform all sorts of experiments. This script chooses the ideal  
asteroid to land on such that from that vantage point the system can monitor the whole asteroid  
constellation within the smallest viewing angle.

## Usage

This script was designed for the Python 2.7.10 interpreter.

Run the script from the command line with a filename containing the asteroid coordinates.

```
python solution.py [path to input file]
```

The files must be formatted as follows:
  * The first line must contain the number of asteroids in the file. All other lines are asteroid coordinates.
  * Each asteroid's coordinates must take the format of: x y. Example: 2 4

## Methodology

Given an asteroid field, the asteroid with the best view of the others will lie somewhere on the 
perimeter of the field. Therefore, to begin with, we must determine which asteroids lie on the perimeter, 
which is known as the "[convex hull](https://en.wikipedia.org/wiki/Convex_hull)" in mathematics. Think of the 
convex hull as the points that would touch an elastic band, if one were stretched around the group of asteroids.

For this solution, we use the [Graham Scan](https://en.wikipedia.org/wiki/Graham_scan) to systematically go 
through the asteroids and determine which ones are on the convex hull. This approach goes asteroid by asteroid, 
going from lowest X to highest X, and determining whether we're making a left, straight, or right turn at each 
point, relative to the vector of the previous two points. If the turn is straight or right, we discard the 
previous asteroid and repeat. Once this process is completed for all the asteroids, we will have the asteroids 
that make up the convex hull.

Next, for each asteroid in the convex hull, we calculate the angle of view between the previous and next
asteroids on the convex hull. Once each asteroid has been assigned its angle of view, we choose the one
with the narrowest angle of view--this is the optimum asteroid to land on.

## Testing

This project was written without a test suite. Instead, you can use the test_solution.py script to 
quickly run all the asteroid files in the test_input_files directory. For each test file, the test script
outputs what we're expecting to see compared to what the actual output is.

