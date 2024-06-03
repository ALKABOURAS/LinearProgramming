import numpy as np
import matplotlib.pyplot as plt


# Define the inequalities constraints
x = np.linspace(0, 20, 400)
y1 = -x + 10  # rearranged from x1 + x2 >= 10 -> x2 >= -x1 + 10
y2 = 10*x + 10  # rearranged from -10x1 + x2 <= 10 -> x2 <= 10x1 + 10
y3 = 4*x + 20  # rearranged from -4x1 + x2 <= 20 -> x2 <= 4x1 + 20
y4 = (-1/4)*x + 5  # rearranged from x1 + 4x2 >= 20 -> x2 >= -1/4*x1 + 5






# Redefine the plot
plt.figure(figsize=(10, 8))

# Recalculate y5 and y6 with correct definitions
y5 = np.maximum(y1, y4)  # Taking the maximum for the constraints that require x2 to be greater
y6 = np.minimum(y2, y3)  # Taking the minimum for the constraints that require x2 to be lesser

# Plot each of the lines
plt.plot(x, y1, label='x1 + x2 ≥ 10', linestyle='-')
plt.plot(x, y2, label='-10x1 + x2 ≤ 10', linestyle='-')
plt.plot(x, y3, label='-4x1 + x2 ≤ 20', linestyle='-')
plt.plot(x, y4, label='x1 + 4x2 ≥ 20', linestyle='-')

# Fill the feasible region
plt.fill_between(x, y5, y6, where=(y5<y6), color='grey', alpha=0.5, label='Feasible Region')

# Define the objective function minZ = 2x1 - x2
# Plot lines of equal cost for the new objective function
Z_values = [0, -10, -20, -30, -40]  # Example Z values for lines of equal cost
for Z in Z_values:
    y_Z = 2*x - Z
    plt.plot(x, y_Z, label=f'Z = {Z}', linestyle='-.')

# Add labels and legend
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('Feasible Region for the Given Constraints')
plt.legend()
plt.xlim(0, 20)
plt.ylim(0, 40)

plt.show()
