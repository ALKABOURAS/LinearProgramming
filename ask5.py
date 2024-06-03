from pulp import *

# Create the LP problem
prob = LpProblem("LP Problem", LpMinimize)

# Define the decision variables
x1 = LpVariable("x1", lowBound=0, cat='Continuous')
x2 = LpVariable("x2", lowBound=0, cat='Continuous')
x3 = LpVariable("x3", lowBound=0, cat='Continuous')

# Set the objective function
prob += 12*x1 - 10*x2 - 30*x3

# Add the constraints
prob += -3*x1 + 2*x2 + 8*x3 <= 17
prob += -1*x1 + 1*x2 + 3*x3 <= 9
prob += -2*x1 + 1*x2 + 8*x3 <= 16

# Solve the LP problem
prob.solve()

# Print the status of the solution
print("Status: ", LpStatus[prob.status])

# Print the optimal values of the decision variables
print("x1 = ", value(x1))
print("x2 = ", value(x2))
print("x3 = ", value(x3))

# Print the optimal value of the objective function
print("Z = ", value(prob.objective))