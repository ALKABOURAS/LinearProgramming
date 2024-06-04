import matplotlib.pyplot as plt
import numpy as np

# Δημιουργία των ευθειών βάσει των περιορισμών
x2 = np.linspace(0, 500, 400) # Περιοχή τιμών για τη μεταβλητή x2

# Περιορισμοί
x1_1 = 3 * x2 # x1 <= 3x2
x1_2 = 500 - x2 # x1 + x2 <= 500
x1_3 = 400 - x2 # x1 + x2 >= 400
x1_4 = 0.4 * x2 / 0.6 # x1 >= 0.4(x1 + x2), επιλύοντας ως προς x1

# Οριοθέτηση της εφικτής περιοχής
plt.figure(figsize=(10, 8))
plt.xlim((0, 500))
plt.ylim((0, 300))
plt.xlabel('$x_1$ (Χυμός Πορτοκαλιού)')
plt.ylabel('$x_2$ (Χυμός Μήλου)')

# Γραφική παράσταση των περιορισμών
plt.plot(x2, x1_1, label=r'$x_1 \leq 3x_2$')
plt.plot(x2, x1_2, label=r'$x_1 + x_2 \leq 500$')
plt.plot(x2, x1_3, label=r'$x_1 + x_2 \geq 400$')
plt.plot(x2, x1_4, label=r'$x_1 \geq 0.4(x_1 + x_2)$')

# Συμπλήρωση της εφικτής περιοχής
y2 = np.minimum(x1_1, x1_2)
plt.fill_between(x2, np.maximum(x1_3, x1_4), y2, where=(y2>=np.maximum(x1_3, x1_4)), color='grey', alpha=0.3)

plt.legend()
plt.show()
