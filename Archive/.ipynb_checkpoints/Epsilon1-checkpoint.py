import numpy as np
import math

# User input
x = float(input("Please enter a value for Bjorken x: "))
Q2 = float(input("Please enter a value for Q-squared: "))

#Set values
E_values = [4.4, 5.5, 6.6, 7.7, 8.8, 11] #GeV
M = 0.938272  # GeV

#Initial calculations
Q2_vs_x = Q2 / x
nu = Q2 / (2 * M * x)

# Print initial values
print("*" * 40)
print(f"For x = {x:.3f}")
print(f"And Q2 = {Q2:.2f}")
#print(f"The ratio of Q2/x is: {Q2_vs_x:.3f}")
#print(f"The value of nu is: {nu:.3f}")
print("-" * 40)

for i, E_val in enumerate(E_values): #enumerating, because I might want to print stuff for only certain iterations
    try:
        Ep = E_val - nu
        if Ep <= 0:
            continue # Discarding invalid Ep
        Ep_val = float(Ep)
        
        #More calculations
        theta_rad = 2 * math.asin(math.sqrt(Q2 / (4 * E_val * Ep_val)))
        theta_deg = math.degrees(theta_rad)
        epsilon = (1 + 2 * (1 + Q2 / (4 * M**2 * x**2)) * (math.tan(theta_rad / 2)**2))**(-1)

        #Printing values for each iteration
        print(f"For E = {E_val:.1f} GeV")
        print(f"E' = {Ep:.3f} GeV")
        print(f"Use Angle >> {theta_deg:.3f} degrees")
        print(f"Epsilon = {epsilon:.3f}")
        print("-" * 40)

        if i == len(E_values) - 1:  # Last iteration
            print("~Fin")

    except ValueError:
        print("Invalid input! Please enter a numerical value.")
