# CS4102 Fall 2019 -- Homework 5
#################################
# Your Computing ID: er6qt
# Collaborators: zh2yn
# Sources: Introduction to Algorithms, Cormen
#################################
import math

class SeamCarving:
    def __init__(self):
        return

    def distance(self, pix1, pix2):
        red = (pix2[0] - pix1[0])
        blue = (pix2[2] - pix1[2])
        green = (pix2[1] - pix1[1])
        return math.sqrt((red) ** 2 + (blue) ** 2 + (green) ** 2)

    def energy(self, image):
        for i in range(image[0]):
            for j in range(image):

                if i == 0:
                    if 0 < j & j < len(image[0])-1:
                        return (self.distance(image[i][j], image[i + 1][j]) + self.distance(image[i][j],image[i][j + 1]) + self. distance(image[i][j], image[i][j - 1])) / 3
                    elif j == 0:
                        return (self.distance(image[i][j], image[i + 1][j]) + self.distance(image[i][j], image[i][j + 1])) / 2
                    else:
                        return (self.distance(image[i][j], image[i][j - 1]) + self.distance(image[i][j], image[i + 1][j])) / 2

                elif i == len(image) - 1:
                    if 0 < j < len(image[0]) - 1:
                        return (self.distance(image[i][j], image[i][j + 1]) + self.distance(image[i][j],image[i][j - 1]) + self.distance(image[i][j], image[i - 1][j])) / 3
                    elif j == 0:
                        return (self.distance(image[i][j], image[i][j + 1]) + self.distance(image[i][j], image[i - 1][j])) / 2
                    else:
                        return (self.distance(image[i][j], image[i][j - 1]) + self.distance(image[i][j], image[i - 1][j])) / 2

                else:
                    if j == 0:
                        return (self.distance(image[i][j], image[i][j + 1]) + self.distance(image[i][j],image[i + 1][j]) + self.distance(image[i][j], image[i - 1][j])) / 3
                    elif j == len(image[0]) - 1:
                        return (self.distance(image[i][j], image[i][j - 1]) + self.distance(image[i][j], image[i + 1][j]) + self.distance(image[i][j], image[i - 1][j])) / 3
                    else:
                        return (self.distance(image[i][j], image[i + 1][j]) + self.distance(image[i][j],image[i][j + 1]) + self. distance(image[i][j], image[i - 1][j]) + self.distance(image[i][j], image[i][j - 1])) / 4


    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    #
    # @return the seam's weight
    def run(self, image):




    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    #
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    #
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array
    def getSeam(self):
        return []