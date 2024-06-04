from scipy.optimize import linprog

# Ορίζουμε τα περιορισμούς του προβλήματος ως λίστες ανισώσεων και τα βάρη της αντικειμενικής συνάρτησης
A = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
b = [2, 2, 4]
c = [-1, -4, -5]

# # Επιλύουμε το πρόβλημα γραμμικού προγραμματισμού με Symplex
# res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
# # print(res)
# #  Τυπώνουμε τη βελτιστη λυση
# print('Optimal value:', round(res.fun*-1, ndigits=2), '\nX:', res.x)
# Solve the problem with the Simplex method and print the optimal solution and the iterations needed
res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='simplex')
print(res)
print('Optimal value:', round(res.fun*-1, ndigits=2), '\nX:', res.x)
print('Number of iterations:', res.nit)