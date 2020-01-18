# CS4102 Fall 2019 -- Homework 2
#################################
# Your Computing ID: er6qt
# Collaborators: zh2yn
# Sources: Introduction to Algorithms, Cormen
#################################
import math;

class ClosestPair:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of closest pair.  It takes as input a list lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest pair distance
    # and return that value from this method
    #
    # @return the distance between the closest pair
    def compute(self, file_data):
        coordinatesx = []

        # Split input file at spaces, and split at a new line to get the set of coordinates
        for i in file_data:
            coord_points = i.split(" ")
            coordinatesx.append((float(coord_points[0]), float(coord_points[1].strip("\n"))))

        coordinatesx = sorted(coordinatesx) #sort x list
        coordinatesy = sorted(coordinatesx, key=lambda y: y[1]) #sorting by 2nd number (sort y list)

        shortest_distance = ClosestPair.recursion_base_cases(self, coordinatesx, coordinatesy)
        return shortest_distance

    def distance(self, coordinate1, coordinate2):
        dist1 = float(coordinate1[0] - coordinate2[0])
        dist2 = float(coordinate1[1] - coordinate2[1])
        return math.sqrt(math.pow(dist1, 2) + math.pow(dist2, 2))

    # Recurse and check base cases of length 2 and 3
    def recursion_base_cases(self, coordinatesx, coordinatesy):
        if len(coordinatesx) == 2:
            return ClosestPair.distance(self, coordinatesx[0], coordinatesx[1])
        elif len(coordinatesx) == 3:
            dist_point1 = ClosestPair.distance(self, coordinatesx[0], coordinatesx[1])
            dist_point2 = ClosestPair.distance(self, coordinatesx[0], coordinatesx[2])
            dist_point3 = ClosestPair.distance(self, coordinatesx[1], coordinatesx[2])
            return min(dist_point1, dist_point2, dist_point3)
        else:
            # Divide: At median x coordinate
            median = (len(coordinatesx)//2)
            middle = int(coordinatesx[median][0])

            split1 = coordinatesx[:median] #split left
            split2 = coordinatesx[median:] #split right

            leftArray = []
            rightArray = []

            for i in coordinatesy: #split coordinatesy list into left and right points
                if (i[0] <= middle):
                    leftArray.append(i)
                if (i[0] > middle):
                    rightArray.append(i)

            # Conquer: Recursively find closest pairs from left and right
            left_points = ClosestPair.recursion_base_cases(self, split1, leftArray)
            right_points = ClosestPair.recursion_base_cases(self, split2, rightArray)

            # Combine: Return min of left and right pairs
            delta = min(left_points, right_points)
            # Creating runway
            runway = []
            for i in coordinatesy:
                if ((middle-delta) <= i[0] <= (middle+delta)):
                    runway.append(i)

            # Get closest pair of points
            smallest_dist = delta
            runway_len = len(runway)
            for i in range(runway_len - 1):
                for j in range(i + 1, min(runway_len, i + 15)):
                    dist = ClosestPair.distance(self, runway[i], runway[j])
                    smallest_dist = min(smallest_dist, dist)
            return smallest_dist