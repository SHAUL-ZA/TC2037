import math

# Function to calculate the area of a square
def calculate_square_area(side):
    area = side ** 2
    return area

# Function to calculate the perimeter of a square
def calculate_square_perimeter(side):
    perimeter = 4 * side
    return perimeter

# Function to calculate the area of a triangle using Heron's formula
def calculate_triangle_area_heron(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    area = math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))
    return area

# Function to calculate the area of a triangle using base and height
def calculate_triangle_area_base_height(base, height):
    area = 0.5 * base * height
    return area

# Function to calculate the perimeter of a triangle
def calculate_triangle_perimeter(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter

# Function to calculate the area of a parallelogram
def calculate_parallelogram_area(base, height):
    area = base * height
    return area

# Function to calculate the perimeter of a parallelogram
def calculate_parallelogram_perimeter(side1, side2):
    perimeter = 2 * (side1 + side2)
    return perimeter

# Function to calculate the area of a trapezoid
def calculate_trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

# Function to calculate the perimeter of a trapezoid
def calculate_trapezoid_perimeter(base1, base2, side1, side2):
    perimeter = base1 + base2 + side1 + side2
    return perimeter

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

# Function to calculate the circumference of a circle
def calculate_circle_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

# Function to calculate the volume of a sphere
def calculate_sphere_volume(radius):
    volume = (4 / 3) * math.pi * radius ** 3
    return volume

# Function to calculate the surface area of a sphere
def calculate_sphere_surface_area(radius):
    surface_area = 4 * math.pi * radius ** 2
    return surface_area

# Function to calculate the area of a cylinder
def calculate_cylinder_area(radius, height):
    area = 2 * math.pi * radius * (radius + height)
    return area

# Function to calculate the volume of a cylinder
def calculate_cylinder_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

# Function to calculate the area of a cone
def calculate_cone_area(radius, slant_height):
    base_area = math.pi * radius ** 2
    lateral_area = math.pi * radius * slant_height
    area = base_area + lateral_area
    return area

# Function to calculate the volume of a cone
def calculate_cone_volume(radius, height):
    volume = (1 / 3) * math.pi * radius ** 2 * height
    return volume

# Perform various mathematical calculations
side = 5
square_area = calculate_square_area(side)
square_perimeter = calculate_square_perimeter(side)

side1 = 3
side2 = 4
side3 = 5
triangle_area_heron = calculate_triangle_area_heron(side1, side2, side3)
triangle_area_base_height = calculate_triangle_area_base_height(side1, side2)
triangle_perimeter = calculate_triangle_perimeter(side1, side2, side3)

base = 6
height = 8
parallelogram_area = calculate_parallelogram_area(base, height)
parallelogram_perimeter = calculate_parallelogram_perimeter(side1, side2)

base1 = 5
base2 = 7
trapezoid_height = 4
trapezoid_area = calculate_trapezoid_area(base1, base2, trapezoid_height)
trapezoid_perimeter = calculate_trapezoid_perimeter(base1, base2, side1, side2)

radius = 4
circle_area = calculate_circle_area(radius)
circle_circumference = calculate_circle_circumference(radius)

sphere_volume = calculate_sphere_volume(radius)
sphere_surface_area = calculate_sphere_surface_area(radius)

cylinder_height = 10
cylinder_area = calculate_cylinder_area(radius, cylinder_height)
cylinder_volume = calculate_cylinder_volume(radius, cylinder_height)

cone_slant_height = 9
cone_area = calculate_cone_area(radius, cone_slant_height)
cone_volume = calculate_cone_volume(radius, cylinder_height)

# Print the results
print("Square - Side:", side)
print("Square Area:", square_area)
print("Square Perimeter:", square_perimeter)

print("\nTriangle (Heron's formula) - Side1:", side1, "Side2:", side2, "Side3:", side3)
print("Triangle Area (Heron's formula):", triangle_area_heron)
print("Triangle Area (Base and Height):", triangle_area_base_height)
print("Triangle Perimeter:", triangle_perimeter)

print("\nParallelogram - Base:", base, "Height:", height)
print("Parallelogram Area:", parallelogram_area)
print("Parallelogram Perimeter:", parallelogram_perimeter)

print("\nTrapezoid - Base1:", base1, "Base2:", base2, "Height:", trapezoid_height)
print("Trapezoid Area:", trapezoid_area)
print("Trapezoid Perimeter:", trapezoid_perimeter)

print("\nCircle - Radius:", radius)
print("Circle Area:", circle_area)
print("Circle Circumference:", circle_circumference)

print("\nSphere - Radius:", radius)
print("Sphere Volume:", sphere_volume)
print("Sphere Surface Area:", sphere_surface_area)

print("\nCylinder - Radius:", radius, "Height:", cylinder_height)
print("Cylinder Area:", cylinder_area)
print("Cylinder Volume:", cylinder_volume)

print("\nCone - Radius:", radius, "Slant Height:", cone_slant_height)
print("Cone Area:", cone_area)
print("Cone Volume:", cone_volume)
