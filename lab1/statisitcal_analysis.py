import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

################
# 1
################
ds = np.array(
    [
        212.3,
        211.5,
        210.8,
        209.8,
        211.1,
        210.6,
        213.2,
        211.7,
        212.6,
        210.3,
        212.1,
        211.5,
        210.6,
        213.0,
        212.1,
        211.7,
        212.1,
        211.3,
        211.8,
        211.4,
        213.4,
        210.5,
        211.0,
        211.1,
        212.7
    ]
)
mean = np.mean(ds)
std = np.std(ds)
b = np.linspace(205, 220, 49)

print(mean)
print(std)
print(ds)

################
# 2
################

plt.hist(ds, bins=b, density=True, label='Measured')
plt.xlabel('Table Length in Cm')
plt.ylabel('Number of measurements (Normalized to 1)')
plt.yticks(range(0,5))
# plt.savefig('figures/612_normalized')


################
# 3
################

x = np.linspace(205,220,200)
def gaussian(x, mu, sigma):
    N0 = 1 / ( sigma * np.sqrt(2 * np.pi) )
    return N0*np.exp(-0.5*((x-mu)/sigma)**2)

gauss = gaussian(x, mean, std)

plt.plot(x, gauss, label='Gaussian from Sample Mean and Std')
# plt.legend()
# plt.savefig('figures/613')


################
# 4
################

mu_fit, sigma_fit = norm.fit(ds)
gauss_fit = gaussian(x, mu_fit, sigma_fit)
plt.plot(x, gauss_fit, '.', label='Gaussian Fit')
plt.legend()
plt.show()
plt.savefig('figures/614')

