import math

def calculate_cube_volume():
    length = float(input("Enter the length of the cube: "))
    return length ** 3

def calculate_sphere_volume():
    radius = float(input("Enter the radius of the sphere: "))
    return (4/3) * math.pi * (radius ** 3)

def calculate_cone_volume():
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    return (1/3) * math.pi * (radius ** 2) * height

def calculate_cylinder_volume():
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    return math.pi * (radius ** 2) * height

def main():
    print("Welcome to your personal 3D volume calculator!")
    choice = input("Press 1 for cube, 2 for sphere, 3 for cone, and 4 for cylinder: ")

    if choice == '1':
        volume = calculate_cube_volume()
        print(f"The 3D volume of the cube is: {volume}")
    elif choice == '2':
        volume = calculate_sphere_volume()
        print(f"The 3D volume of the sphere is: {volume}")
    elif choice == '3':
        volume = calculate_cone_volume()
        print(f"The 3D volume of the cone is: {volume}")
    elif choice == '4':
        volume = calculate_cylinder_volume()
        print(f"The 3D volume of the cylinder is: {volume}")
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()



