import math
from turtle import width

@beartype # type checking decorator
def circle_area(radius: float) -> float:
    
    
    """
    Calculate the area of a circle.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.

    """
    return math.pi * radius ** 2

@beartype 
def rectangle_perimeter(width: float, height: float) -> float:  
    
    """
    Calculate the area of a rectangle.
    
    Parameters:
    width (float): The width of the rectangle.
    height (float): The height of the rectangle.
    
    Returns:
    float: The perimeter of the rectangle.

    """
    return 2 * (width + height)

@beartype
def triangle_area(base: float, height: float) -> float:
    """
    Calculate the area of a triangle.
    
    Parameters:
    base (float): The base of the triangle.
    height (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.

    """
    return 0.5 * base * height

circle_area(5.0)
rectangle_perimeter(4.0, 6.0)
triangle_area(3.0, 7.0)