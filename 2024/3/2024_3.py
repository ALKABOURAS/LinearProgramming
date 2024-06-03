from pulp import *

initial_times = [7, 10, 5, 3, 8, 7]  # Αρχικοί χρόνοι για τις εργασίες Ε1 έως Ε6
min_times = [5, 5, 5, 1, 6, 4]       # Ελάχιστοι δυνατοί χρόνοι για τις εργασίες
costs = [6, 10, 0, 8, 8, 3]          # Κόστος μείωσης ανά εβδομάδα για τις εργασίες

# Δημιουργία του μοντέλου
model = LpProblem("Minimize_Cost", LpMinimize)

# Δημιουργία μεταβλητών απόφασης για τον χρόνο μείωσης κάθε εργασίας
x = LpVariable.dicts("reduction_time", list(range(6)), lowBound=0)

# Προσθήκη της αντικειμενικής συνάρτησης στο μοντέλο
model += lpSum([costs[i] * x[i] for i in range(6)])

# Προσθήκη περιορισμών για τους ελάχιστους και μέγιστους χρόνους ολοκλήρωσης
for i in range(6):
    model += x[i] <= initial_times[i] - min_times[i], "Max_reduction_%d" % i

# Περιορισμός για τον συνολικό χρόνο διεκπεραίωσης (υποθετικός, πρέπει να προσαρμοστεί)
# model += Συνθήκη για συνολικό χρόνο <= 19 εβδομάδες

# Λύση του μοντέλου
model.solve()

# Εκτύπωση αποτελεσμάτων
print("Κατάσταση:", LpStatus[model.status])
print("Συνολικό Κόστος:", value(model.objective))
for v in model.variables():
    print(v.name, "=", v.varValue)
