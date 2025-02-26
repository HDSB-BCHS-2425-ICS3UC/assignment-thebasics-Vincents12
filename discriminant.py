
print("Welcome to your personal Discriminant Calculator!")
print("-------Please follow the steps ahead-------")
print(input("Press Enter"))
# Input of the coefficients 
a = float(input("Enter the coefficient for a: "))
# Let's the user put in the float for coefficient: a
b = float(input("Enter the coefficient for b: "))
# Let's the user put in the float for coefficient: b
c = float(input("Enter the coefficient for c: "))
# Let's the user put in the float for coefficient: c


# Calculation of the discriminant
delta = b**2 - 4 * a * c

# Output of the result
print (f"The discriminant of the calculation is: {delta}")