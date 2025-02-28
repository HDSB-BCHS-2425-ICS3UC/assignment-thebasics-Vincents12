import math 
#So that special math characters work like math.pi

# The calculation block of the cube
def calculate_cube_volume(): 
    length = float(input("Enter the length of the cube: ")) 
    return length ** 3 


# The calculation block of the sphere
def calculate_sphere_volume():
    radius = float(input("Enter the radius of the sphere: "))
    return (4/3) * math.pi * (radius ** 3) 



# The calculation block of the cone
def calculate_cone_volume():
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    return (1/3) * math.pi * (radius ** 2) * height 


# The calculation block of the cylinder
def calculate_cylinder_volume():
    radius = float(input("Enter the radius of the cylinder: ")) 
    height = float(input("Enter the height of the cylinder: ")) 
    return math.pi * (radius ** 2) * height 
if input: str


# Main start of output
def main():
    print("Welcome to your personal 3D volume calculator!")
    try:
        choice = input("Press 1 for cube, 2 for sphere, 3 for cone, and 4 for cylinder: ")
# The choice for the user to select which 3D volume they want to calculate
   
    except ValueError: # If the user enters a str
        print()
        print()
        print("Invalid input! Please try again.")
        print()
        print()
        main()  # Restart the program if you get the error message


    if choice == '1':
        volume = calculate_cube_volume() # Cube volume output
        print(f"The 3D volume of the cube is: {volume}")


    elif choice == '2':
        volume = calculate_sphere_volume() # Sphere volume output
        print(f"The 3D volume of the sphere is: {volume}")


    elif choice == '3':
        volume = calculate_cone_volume() # Cone volume output
        print(f"The 3D volume of the cone is: {volume}")


    elif choice == '4':
        volume = calculate_cylinder_volume() # Cylinder volume calculating
        print(f"The 3D volume of the cylinder is: {volume}")
    
# Else in case the user enters something invalid
    else:
        print("Invalid choice. Please select a valid option.")    

if __name__ == "__main__":
    main()
# So main is organzied



