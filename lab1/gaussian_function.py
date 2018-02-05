import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

###############
# 1
###############

x = np.linspace(-6, 6, 150)

def gaussian(x, N0, mu, sigma):
    return N0*np.exp(-0.5*((x-mu)/sigma)**2)

sigma = 2
mu = 0
N0 = 1 / ( sigma * np.sqrt(2 * np.pi) )
f = gaussian(x, N0, mu, sigma)
g = gaussian(x, N0, mu + 1, sigma / 2)

plt.plot(x, f,label='original')
plt.plot(x, g,'o', markersize=1, label='shifted')
plt.legend()
# plt.show()
plt.savefig('figures/gaussian.png')


###############
# 2
###############

inf = 10 * sigma
lower_bound = - inf
upper_bound = inf
I = quad(gaussian, lower_bound, upper_bound, args=(N0, mu, sigma))

print(I)


###############
# 3
###############

def x_gauss(x, N0, mu, sigma):
    return x * N0*np.exp(-0.5*((x-mu)/sigma)**2)

J = quad(x_gauss, lower_bound, upper_bound, args=(N0, mu, sigma))

print(J)


###############
# 4
###############

lower_bound = - inf
upper_bound = mu - sigma
below_envelope = quad(gaussian, lower_bound, upper_bound, args=(N0, mu, sigma))

lower_bound = mu + sigma
upper_bound = inf
above_envelope = quad(gaussian, lower_bound, upper_bound, args=(N0, mu, sigma))

print(below_envelope[0] + above_envelope[0])


