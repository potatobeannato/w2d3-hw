def say_hello(name):
    print(f"Hello {name}")

def say_goodbye(name):
    print(f"Goodbye {name}")
    


                               
import math

def AreaofHouse(width, height):
    Area = width * height
    print("Area of a Rectangle is: %.2f" %Area)   #%.2f is to represent a place holder for floating numbers when calculated
     
width = float(input('Please Enter the Width of a Rectangle: '))
height = float(input('Please Enter the Height of a Rectangle: '))
 
AreaofHouse(width, height)



def CircumferenceofCircle(circumference):
    circumference = 2 * math.pi * radius
    print("Circumference Of a Circle = %.2f" %circumference)
    
radius = float(input('Please Enter the radius of a circle: '))    
CircumferenceofCircle(radius)