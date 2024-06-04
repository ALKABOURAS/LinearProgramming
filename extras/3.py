from pulp import *

# Δημιουργία του μοντέλου
model = LpProblem("Minimize_Cost", LpMinimize)

# Αρχικοί χρόνοι και ελάχιστοι χρόνοι για κάθε εργασία
initial_times = [7, 10, 5, 3, 8, 7]
min_times = [5, 5, 5, 1, 6, 4]

# Κόστος μείωσης ανά εβδομάδα για κάθε εργασία
costs = [6, 10, 0, 8, 8, 3]

# Μεταβλητές απόφασης: χρόνος μείωσης για κάθε εργασία
x = LpVariable.dicts("reduction", range(1, 7), lowBound=0)

# Ορισμός της αντικειμενικής συνάρτησης
model += lpSum([costs[i] * x[i+1] for i in range(6)])

# Προσθήκη περιορισμών μείωσης χρόνου για κάθε εργασία
for i in range(6):
    model += x[i+1] <= initial_times[i] - min_times[i], f"Max_reduction_{i+1}"

# Συνολικοί χρόνοι ολοκλήρωσης για κάθε σετ εργασιών (εκτελούνται ταυτόχρονα)
T1 = max(initial_times[0] - x[1], initial_times[1] - x[2])
T2 = max(initial_times[2] - x[3], initial_times[3] - x[4])
T3 = max(initial_times[4] - x[5], initial_times[5] - x[6])

# Περιορισμός για τον συνολικό απαιτούμενο χρόνο
model += lpSum([T1, T2, T3]) <= 19, "Total_time"

# Λύση του προβλήματος
model.solve()

# Εμφάνιση αποτελεσμάτων
print("Κατάσταση:", LpStatus[model.status])
print("Συνολικό Κόστος Μείωσης: ", value(model.objective))
for v in model.variables():
    print(v.name, "=", v.varValue)
print("Συνολικός Χρόνος Ολοκλήρωσης: ", value(T1 + T2 + T3))
