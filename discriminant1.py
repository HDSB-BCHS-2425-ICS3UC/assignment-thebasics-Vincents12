# Start of main 
def main():
    print("Welcome to your personal Discriminant Calculator!")
    print("-------Please follow the steps ahead-------")
    print()
    print (input("Press Enter to continue..."))

    try:
        # Input of the coefficients
        a = float(input("Enter the coefficient for a: "))
        b = float(input("Enter the coefficient for b: "))
        c = float(input("Enter the coefficient for c: "))

        # Calculation of the discriminant
        delta = b**2 - 4 * a * c

        # Output of the result
        print(f"The discriminant is: {delta}")

    except ValueError: # If the user enters a str
        print()
        print()
        print("Invalid input! Please try again.")
        print()
        print()
        main()  # Restart the program if you get the error message

if __name__ == "__main__":
    main()
# So main is organzied
