# Assignment Two
# By Emil Granrud Gabrielli
# For NTNU Web course IFUD1056: Python for programmers (Vår 2019)
#
# In this assignment, you are asked to write a code to estimate pi using Archimedes method
#
# Archimedes estimated pi using polygons.

def estimate_pi():
    
    polygon_sides = [6, 12, 24, 48, 96, 192, 384]
    
    side_len = 1
    
    for polygon in polygon_sides:
        
        side_half = side_len/2
        a = (1-(side_half**2))**0.5
        b = 1 - a
        
        perimeter = polygon * side_len
        
        estimate_pi = perimeter / 2
        
        print(f"Estimated Pi with a polygon of {polygon} is {estimate_pi}")
        
        side_len = ((b**2)+(side_half**2))**0.5
        
print(estimate_pi())