from pulp import *

# Create the model
model = LpProblem("Minimize_Cost", LpMinimize)

# Initial times and minimum times for each task
initial_times = [7, 10, 5, 3, 8, 7]
min_times = [5, 5, 5, 1, 6, 4]

# Reduction cost per week for each task
costs = [6, 10, 0, 8, 8, 3]

# Decision variables: reduction time for each task
x = LpVariable.dicts("reduction", range(1, 7), lowBound=0)

# Define the objective function
model += lpSum([costs[i] * x[i+1] for i in range(6)])

# Add reduction time constraints for each task
for i in range(6):
    model += x[i+1] <= initial_times[i] - min_times[i], f"Max_reduction_{i+1}"

# Total completion times for each set of tasks (executed simultaneously)
T = LpVariable.dicts("T", range(1, 4), lowBound=0)

# Constraints to model the max function
model += T[1] >= initial_times[0] - x[1]
model += T[1] >= initial_times[1] - x[2]
model += T[2] >= initial_times[2] - x[3]
model += T[2] >= initial_times[3] - x[4]
model += T[3] >= initial_times[4] - x[5]
model += T[3] >= initial_times[5] - x[6]

# Constraint for the total required time
model += lpSum([T[1], T[2], T[3]]) <= 19, "Total_time"

# Solve the problem
model.solve()

# Display results
print("Status:", LpStatus[model.status])
print("Total Reduction Cost: ", value(model.objective))
for v in model.variables():
    print(v.name, "=", v.varValue)
print("Total Completion Time: ", value(T[1] + T[2] + T[3]))