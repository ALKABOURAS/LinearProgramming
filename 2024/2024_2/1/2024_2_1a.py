from scipy.optimize import linprog

# 1.a
def solve_linear_programming(c, A, b, bounds):
    # Solving the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='simplex')
    return res

# 1.b
def solve_perturbed_linear_programming(c, A, b, bounds, Delta):
    # Perturbing coefficient of x2 (basic variable) by Delta
    c_perturbed_basic = c.copy()
    c_perturbed_basic[1] -= Delta

    # Solving the linear programming problem with perturbed objective function
    result_perturbed_basic = linprog(c_perturbed_basic, A_ub=A, b_ub=b, bounds=bounds, method='simplex')
    return result_perturbed_basic


# Coefficients of the objective function
c = [-5, -3, -1, -4]

# Coefficients of the inequality constraints
A = [
    [1, -2, 2, 3],
    [2, 2, 2, -1],
    [3, 1, -1, 1],
    [0, -1, 2, 2]
]

# Right-hand side values
b = [10, 6, 10, 7]

# Bounds for the variables
bounds = [(0, None), (0, None), (0, None), (0, None)]

# Call the functions
res = solve_linear_programming(c, A, b, bounds)
print(res)

res_perturbed = solve_perturbed_linear_programming(c, A, b, bounds, 0.5)
print(res_perturbed)
