# WAP to calculate the area of triangle, rectangle, circle, sphere.

base = int(input("Enter the value of base (cm): "))
height= int(input("Enter the value of height (cm): "))
length = int(input("Enter the value of length (cm): "))
breath = int(input("Enter the value of breath (cm): "))
radius = int(input("Enter the value of radius (cm): "))
π = 3.14

Triangle = int((1/2)*base*height)
Rectangle = int(length*breath)
Circle = int(π*radius*radius)
Sphere = int(4*π*radius*radius)

print(f"The area of Triangle is {Triangle}cm")
print(f"The area of Rectangle is {Rectangle}cm")
print(f"The area of Circle is {Circle}cm")
print(f"The area of Sphere is {Sphere}cm")