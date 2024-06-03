import matplotlib.pyplot as plt
import numpy as np
from pulp import *

# Define the problem
prob = LpProblem("Linear_Programming_Problem", LpMaximize)

# Define the decision variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)

# Define the objective function
prob += 2*x1 - 3*x2

# Define the constraints
prob += 2*x1 + x2 >= 4
prob += x1 + 2*x2 >= 5
prob += x1 - 2*x2 <= 1

# Solve the problem
prob.solve()

# Print the status of the solution
print("Status: ", LpStatus[prob.status])

# Print the optimal values of the decision variables
print("x1 = ", value(x1))
print("x2 = ", value(x2))

# Print the optimal value of the objective function
print("Optimal value of the objective function: ", value(prob.objective))

# Define the points for the plot
x = np.linspace(0, 4, 100)
y1 = 4 - 2*x
y2 = (5 - x)/2
y3 = (x + 1)/2

# Plot the feasible region
plt.figure(figsize=(8, 8))
plt.plot(x, y1, 'r', label=r'$2x_1+x_2=4$')
plt.plot(x, y2, 'g', label=r'$x_1+2x_2=5$')
plt.plot(x, y3, 'b', label=r'$x_1-2x_2=1$')
plt.fill_between(x, y1, y2, where=y1>=y2, interpolate=True, color='grey', alpha=0.5)
plt.fill_between(x, y2, y3, where=y2<=y3, interpolate=True, color='grey', alpha=0.5)
plt.xlim(0, 4)
plt.ylim(0, 3)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.legend(loc='best')
plt.grid()

plt.show()