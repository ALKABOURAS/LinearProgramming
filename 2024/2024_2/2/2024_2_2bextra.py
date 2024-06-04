import numpy as np

# Define the basis matrix B
B = np.array([
    [1, 3, -4, 0, 0, 0, 0],
    [3, -3, -1, 0, 0, 0, 0],
    [2, 0, -2, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, -1],
    [0, 1, 0, 0, 0, 0, 0]
])

# Define the right-hand side vector b
b = np.array([-6, 2, -5, -2, 10, 5, 25])

# Compute the basic solution for the primal problem
x_B = np.linalg.solve(B, b)
print("Basic solution for the primal problem:")
print(x_B)

# Define the matrix A for the dual problem
A = np.array([
    [0, 1, 2, 1, 1, 0, 0],
    [0, -1, 3, 0, 0, 1, 1],
    [1, 3, -3, 2, 0, 0, 0],
    [0, -4, -1, -2, 0, 0, 0]
]).T

# Define the cost vector c
c = np.array([3, -2, -5, 7, 8])

# Extract the basis matrix B_C for the dual problem
B_C = A[:, [1, 3, 4, 6]]

# Compute the basic solution for the dual problem
y_B = np.linalg.solve(B_C.T, c)
print("Basic solution for the dual problem:")
print(y_B)

# Verify complementary slackness
primal_nonzero_indices = [1, 3, 4, 6]
dual_nonzero_indices = [0, 2, 5]

complementary_slackness = True

for i in primal_nonzero_indices:
    if np.dot(A[:, i], y_B) != c[i]:
        complementary_slackness = False

for j in dual_nonzero_indices:
    if np.dot(B[j], x_B) != b[j]:
        complementary_slackness = False

print("Complementary slackness holds:" if complementary_slackness else "Complementary slackness does not hold.")
