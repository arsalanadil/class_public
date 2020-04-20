import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/arsalanadil/Desktop/CLASS/class_public/output/quint_in115_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['quint_in115_background']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = ['w_scf']
#tex_names = ['(8\\pi G/3)rho_scf', '(8\\pi G/3)p_scf']
x_axis = 'z'
ylim = []
xlim = []

zlist = curve[:,0]
alist = 1/(zlist+1)
#ax.loglog(alist, curve[:,13])
#ax.loglog(alist, curve[:,8])
#ax.loglog(alist, curve[:,6])
ax.semilogx(alist,curve[:,14]/curve[:,13])

#ax.legend([root+': '+elem for (root, elem) in
 #   itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('a', fontsize=16)
plt.show()
