import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
y = np.exp(-x)

data_out = np.column_stack((x, y))
np.savetxt('output.dat', data_out)

u, v = np.loadtxt('output.dat', unpack=True)
plt.plot(u, v)
plt.xlabel('Dummy Label')
plt.ylabel('Dummy Label')
plt.savefig('figures/figure4')
plt.show()
