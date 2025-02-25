import math

# Function to calculate the volume of a cube
def volume_cube(length):
    return length ** 3

# Function to calculate the volume of a sphere
def volume_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

# Function to calculate the volume of a cylinder
def volume_cylinder(radius, height):
    return math.pi * (radius ** 2) * height

# Function to calculate the volume of a cone
def volume_cone(radius, height):
    return (1/3) * math.pi * (radius ** 2) * height

# Main program
def main():
    print("Welcome to the Volume Calculator!")
    print("--------------------------------")

    # Cube
    length = float(input("Enter the length of the cube: "))
    cube_volume = volume_cube(length)
    print(f"\nThe volume of the cube with length {length} is: {cube_volume:.2f}")

    # Sphere
    radius_sphere = float(input("\nEnter the radius of the sphere: "))
    sphere_volume = volume_sphere(radius_sphere)
    print(f"The volume of the sphere with radius {radius_sphere} is: {sphere_volume:.2f}")

    # Cylinder
    radius_cylinder = float(input("\nEnter the radius of the cylinder: "))
    height_cylinder = float(input("Enter the height of the cylinder: "))
    cylinder_volume = volume_cylinder(radius_cylinder, height_cylinder)
    print(f"The volume of the cylinder with radius {radius_cylinder} and height {height_cylinder} is: {cylinder_volume:.2f}")

    # Cone
    radius_cone = float(input("\nEnter the radius of the cone: "))
    height_cone = float(input("Enter the height of the cone: "))
    cone_volume = volume_cone(radius_cone, height_cone)
    print(f"The volume of the cone with radius {radius_cone} and height {height_cone} is: {cone_volume:.2f}")

    print("\nThank you for using the Volume Calculator!")

# Run the program
if __name__ == "__main__":
    main()