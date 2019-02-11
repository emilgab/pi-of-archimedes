# Assignment Two
# By Emil Granrud Gabrielli
# For NTNU Web course IFUD1056: Python for programmers (Vår 2019)
#
# In this assignment, you are asked to write a code to estimate pi using Archimedes method
#
# Archimedes estimated pi using polygons.

def estimate_pi():
    
    """
    A function which iterates through a list of Polygons (with sides ranging from 6 to 384) and returns the estimate of pi using Archimedes' method.
    """
    
    # Our polygons where the sides are the double of the previous polygon.
    polygon_sides = [6, 12, 24, 48, 96, 192, 384]
    
    # Length of the side (radius of the circle), starts at 1 with a polygon of 6 sides.
    side_len = 1
    
    for polygon in polygon_sides:
        
        side_half = side_len/2
        
        # Pythagorean theorem
        a = (1-(side_half**2))**0.5
        b = 1 - a
        
        perimeter = polygon * side_len
        
        estimate_pi = perimeter / 2
        
        print(f"Estimated Pi with a polygon of {polygon} sides is {estimate_pi}")
        
        # Changes the side_len variable for our next estimate of pi, with double the amount of sides.
        side_len = ((b**2)+(side_half**2))**0.5
        
estimate_pi()