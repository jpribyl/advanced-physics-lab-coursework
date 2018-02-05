import matplotlib.pyplot as plt
import numpy as np

g = -9.8
t = np.linspace(1, 10, 20)
print(t)

y = 1000 + g*t**2/2
print(y)

plt.plot(t, y)
plt.savefig('figures/figure1.png')

plt.clf()
err = .05*y
plt.errorbar(t, y, yerr=err, fmt='o')
t_theory = np.linspace(0, 11, 56)
y_theory = 1000 + g*t_theory**2/2
plt.plot(t_theory, y_theory)
plt.savefig('figures/figure2.png')


plt.clf()
err = .05*y
t_theory = np.linspace(0, 11, 56)
y_theory = 1000 + g*t_theory**2/2

plt.errorbar(t, y, yerr=err, fmt='o')

# changing color, size, and symbol as required
plt.plot(t_theory, y_theory, 'r.', MarkerSize=1)

# labelling axes
plt.xlabel('time (s)')
plt.ylabel('height (m)')

# add a legend
plt.legend(['Theory', 'Actual'])
# plt.show()
plt.savefig('figures/figure3.png')




