import numpy as np
from scipy.optimize import linprog

# Δεδομένα του προβλήματος
c = [-3, 2, 5, -7, -8]  # Συντελεστές της αντικειμενικής συνάρτησης
A_eq = [
    [0, 1, -1, 3, -4],
    [2, 3, -3, -1, 0],
    [1, 0, 2, -2, 0]
]
b_eq = [-6, 2, -5]

A_ub = [
    [1, 0, 0, 0, 0],
    [-1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, -1, 0, 0, 0]
]
b_ub = [10, 2, 25, 5]

# Λύση του πρωτεύοντος προβλήματος
res_primal = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub,
                     bounds=[(None, None), (5, 25), (0, None), (0, None), (0, None)],
                     method='simplex')

# Εκτύπωση των αποτελεσμάτων
print("Πρωτεύουσα Λύση:")
print(res_primal)

# Δημιουργία του δυϊκού προβλήματος
c_dual = b_eq
A_dual = np.transpose(A_eq)
b_dual = -np.array(c)

# Λύση του δυϊκού προβλήματος
res_dual = linprog(c_dual, A_ub=A_dual, b_ub=b_dual,
                   bounds=[(0, None)]*len(c_dual), method='simplex')

# Εκτύπωση των αποτελεσμάτων
print("Δυϊκή Λύση:")
print(res_dual)
