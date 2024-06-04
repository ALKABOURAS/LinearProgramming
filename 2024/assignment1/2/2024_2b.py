import numpy as np
import matplotlib.pyplot as plt

# Define the inequalities constraints
x = np.linspace(0, 600, 400)
y1 = 0.25/0.75*x  # rearranged from x1 <= 3x2
y2 = 500 - x  # rearranged from x1 + x2 <= 500
y3 = 400 - x  # rearranged from x1 + x2 >= 400
y4 = 250  # rearranged from x2 <= 250
# Για το Β ερώτημα y5 = x
y5 = x

# Initialize the plot
plt.figure(figsize=(10, 8))

# Plot each of the lines representing the constraints
plt.plot(x, y1, label='x1 <= 3x2', linestyle='-')
plt.plot(x, y2, label='x1 + x2 <= 500', linestyle='-')
plt.plot(x, y3, label='x1 + x2 >= 400', linestyle='-')
plt.plot(x, [y4]*len(x), label='x2 <= 250', linestyle='-')
plt.plot(x, y5, label='x1 - χ2 >= 0', linestyle='-')

# Identifying the feasible region more accurately
# Assuming y2 and y3 are the main bounds and y4 is a horizontal line constraint
y_lower = np.maximum(y3, y1)  # Lower bound is the higher value of y3 or 0, for x2 >= constraints
y_upper = np.minimum(y4, y2)# Upper bound is the lower of y2 and y4, for x2 <= constraints
y_upper2 = np.minimum(y2, y5)
y_upper = np.minimum(y_upper, y_upper2)

# Fill the feasible region
# We don't use y5 or y1 directly here because they form boundaries not directly involved in the fill
plt.fill_between(x, y_lower, y_upper, where=(y_upper>=y_lower), color='grey', alpha=0.5, label='Feasible Region')

# Define the objective function maxZ = 5(x1 + x2) - 2x1 - x2
# Plot lines of equal cost for the new objective function
Z_values = [0, 500, 1000, 1250, 1500, 1750]  # Example Z values for lines of equal cost
for Z in Z_values:
    y_Z = (Z - 3*x)/4 # rearranged from 5(x1 + x2) - 2x1 - x2 = Z
    plt.plot(x, y_Z, label=f'Z = {Z}', linestyle='--', linewidth=5)

# Add labels, legend, and set limits
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('Feasible Region for the Given Constraints')
plt.legend()
plt.xlim(0, 600)
plt.ylim(0, 300)  # Adjusted for visibility based on the constraint values

plt.show()