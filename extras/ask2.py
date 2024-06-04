import pulp
import numpy as np
import matplotlib.pyplot as plt

# Create the problem instance
prob = pulp.LpProblem("Product Design Problem", pulp.LpMinimize)

# Define the decision variables
x = pulp.LpVariable('x', lowBound=0)
y = pulp.LpVariable('y', lowBound=0)

# Define the objective function
prob += 6*x + 7.5*y

# Define the constraints
prob += 6*x + 4.5*y >= 5.1
prob += 6*x + 9*y <= 8.4
prob += 12*x + 9*y <= 10.8
prob += x + y == 1

# Solve the problem
status = prob.solve()

# Print the results
if status == pulp.LpStatusOptimal:
    print(f"Optimal solution found: x={x.value():.2f} (grams of G1), y={y.value():.2f} (grams of G2), with a cost of {prob.objective.value():.2f} monetary units.")
else:
    print("Could not find an optimal solution.")

# Define the constraints as inequalities
x_range = np.linspace(0, 2, 100)
y1 = (5.1 - 6*x_range)/(-4.5)
y2 = (8.4 - 6*x_range)/9
y3 = (10.8 - 12*x_range)/9
y4 = np.minimum(np.maximum(0, 1 - x_range), (10.8 - 12*x_range)/9)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_range, y1, label=r'$6x + 4.5y \geq 5.1$')
ax.plot(x_range, y2, label=r'$6x + 9y \leq 8.4$')
ax.plot(x_range, y3, label=r'$12x + 9y \leq 10.8$')
ax.fill_between(x_range, y4, 2, color='gray', alpha=0.3, label='Feasible Region')
ax.scatter(x.value(), y.value(), s=100, c='red', label='Optimal Solution')
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
ax.set_xlabel(r'$x$ (grams of G1)')
ax.set_ylabel(r'$y$ (grams of G2)')
ax.set_title('Feasible Region for Product Design Problem')
ax.legend(loc='lower right')
plt.show()