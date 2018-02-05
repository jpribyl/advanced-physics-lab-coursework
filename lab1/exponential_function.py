import matplotlib.pyplot as plt
import numpy as np

###############
# 1
###############
mu = .5
x = np.linspace(0, 10, 50)
y = np.exp( -1 * mu * x)

plt.plot(x, y, label='y = e ^ (- mu x)')
plt.xlabel('x in units')
plt.ylabel('y in units')
plt.legend()
# plt.show()
plt.savefig('figures/exponential.png')

plt.clf()
plt.plot(x, y, label='y = e ^ (- mu x)')
plt.xlabel('x in units')
plt.ylabel('y in units')
plt.yscale('log')
plt.legend()
# plt.show()

# mu is 1 / slope
plt.savefig('figures/exponential_log.png')


###############
# 2
###############

# in exponential decay, mu is the decay rate - IE how fast decay occurs
# in a circuit, mu is the inverse of the time constant - IE related inversely
# to how quickly voltage will fall



