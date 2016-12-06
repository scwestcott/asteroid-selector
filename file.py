#!/usr/bin/python

class File(object):
    """Parse a file with asteroid count and coordinate information.

    Attributes:
        lines_as_strings: A list of the lines in the file as strings.
        lines_as_coordinates: A list of coordinate lists. Each list item is itself a list with
            the x and y in float format.
        expected_asteroid_count: Expected number of asteroids, according to first line of the file.
        actual_asteroid_count: The actual number of asteroids found in the file.
    """

    lines_as_strings = []
    lines_as_coordinates = []
    expected_asteroid_count = None
    actual_asteroid_count = None

    def __init__(self, filename):
        """Parse the lines of the file, trim and validate the data."""
        self.lines_as_strings = [line.rstrip('\n') for line in open(filename)]
        
        # Trim any extra whitespace in the file and valdiate the data.
        self.trim()
        self.validate_data()

    def is_float(self, value):
        """"Check that the given value is a float"""
        try:
            float(value)
            return True
        except ValueError:
            return False

    def is_integer(self, value):
        """"Check that the given value an integer"""
        try:
            int(value)
            return True
        except ValueError:
            return False

    def trim(self):
        """Remove beginning and trailing whitespace, plus any extra spaces between coord_string."""
        for key, line in enumerate(self.lines_as_strings):
            self.lines_as_strings[key] = ' '.join(line.split())

    def validate_data(self):
        """Validate file data. If errors are found, print to standard error and exit."""
        import sys

        # Check that the file contains at least two lines of data.
        if not len(self.lines_as_strings) > 1:
            sys.stderr.write("Error: File does not contain any data.\n")
            sys.exit(1)

        # If the file contains data, pull out the first line as the expected asteroid count.
        self.expected_asteroid_count = self.lines_as_strings.pop(0)

        # Check that the expected asteroid count is an integer.
        if not self.is_integer(self.expected_asteroid_count):
            sys.stderr.write("Error: Expected asteroid count is a non-integer: %s\n" % self.expected_asteroid_count)
            sys.exit(1)
        else:
            self.expected_asteroid_count = int(self.expected_asteroid_count)

        # For the rest of the file, validate coordinate data, convert to floats, and assign to lines_as_coordinates.
        lines_dict = {}
        for line in self.lines_as_strings:
            if line in lines_dict:
                sys.stderr.write("Error: Two asteroids found at %s. Only one asteroid may exist per location.\n" % line)
                sys.exit(1)
            else:
                lines_dict[line] = 1

            coord_string = line.split()
            if len(coord_string) != 2:
                sys.stderr.write("Error: %d coordinates in asteroid %s %s. Expected exactly 2.\n" 
                    % (len(coord_string), coord_string[0], coord_string[1]))
                sys.exit(1)
            if not self.is_float(coord_string[0]) or not self.is_float(coord_string[1]):
                sys.stderr.write("Error: An asteroid contains a non-numeric coordinate: %s %s\n" 
                    % (coord_string[0], coord_string[1]))
                sys.exit(1)

            coordinates = [float(coord_string[0]), float(coord_string[1])]
            self.lines_as_coordinates.append(coordinates)

        # Now that coordinates have been parsed, compare actual count to expected count.
        self.actual_asteroid_count = len(self.lines_as_coordinates)

        if self.expected_asteroid_count != self.actual_asteroid_count:
            sys.stderr.write("Error: Expected %d asteroids but got %d.\n" 
                % (self.expected_asteroid_count, self.actual_asteroid_count))
            sys.exit(1)
        # We need > 3 asteroids to continue. If we only have 2 asteroids, they will both have the exact same
        # field of view of the other: 0 degrees.
        elif self.actual_asteroid_count < 3:
            sys.stderr.write("Error: There are only %d asteroids. There must be at least 3.\n" 
                % self.actual_asteroid_count)
            sys.exit(1)
