import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import curve_fit

################
# 1
################

ds = np.array([212.3, 211.5, 210.8, 209.8, 211.1, 210.6, 213.2, 211.7, 212.6, 210.3, 212.1,
    211.5, 210.6, 213.0, 212.1, 211.7, 212.1, 211.3, 211.8, 211.4, 213.4,
    210.5, 211.0, 211.1, 212.7])

x = np.array([-2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
y = np.array([17.3, 18.9, 10.3, 11.4, 2.7, 3.7, -3.5, -4.0, -7.9, -12.1, -17.3, -15.9])
y_err = np.array([2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0])

################
# 2
################
plt.errorbar(x, y, fmt='.', yerr=y_err, label='measured points')
x_est = np.linspace(-2, 9, 50)
y_est = -4.0 * x_est + 14
plt.plot(x_est, y_est, label='estimated fit')


# plt.savefig('figures/622.png')


################
# 3
################

def func_to_fit(x, a, b):
    return a*x + b
popt, pcov = curve_fit(func_to_fit, x, y, sigma=y_err, p0=None)
y_fit = func_to_fit(x, *popt)

plt.plot(x_est, func_to_fit(x_est, *popt), '.r', label='curve_fit')
# plt.plot(x, y_fit)
plt.xlabel('x - data')
plt.ylabel('y - data')
plt.legend()
plt.savefig('figures/623.png')
# plt.show()


################
# 4
################
print('number of points:')
print(len(x))
# plt.show()

# for my estimated fit: 7 / 12 points
# for curve_fit: ~ 8 / 12 points hit



################
# 5
################

chi2 = np.sum(((y-func_to_fit(x, *popt))/y_err)**2) / (12 - 2)
print('chi^2: ')
print(chi2)


################
# 6
################

y_est_lo = -2.0 * x_est + 8.2
y_est_hi = -6.0 * x_est + 19
plt.plot(x_est, y_est_lo, '^', label='lowest estimated fit')
plt.plot(x_est, y_est_hi, 'o', label='highest estimated fit')
plt.legend()
plt.savefig('figures/626')
plt.show()


# slope uncertainty ~ 2
# intercept uncertainty ~ 5.5

################
# 7
################
parameter_uncertainty = np.sqrt(np.diag(pcov))

# first is slope, second is intercept
print('parameter uncertainty: ') 
print(parameter_uncertainty)


################
# 8
################

'''
When we raise y_err by a factor of 4, chi^2 decreases noticeably (1.28 to
.08)

Likewise, when we lower y_err, chi^2 increases to ~20

We can interpret lower chi^2 as achieving a "better" fit. However, .08
is "too good" of a fit. Practically speaking, we increased the uncertainty in
our measurement enough that our model intersects almost every single point 

Higher chi^2 >> 1 indicates that the data is not well fit by the function (or
that estimated error is too small)

parameters and parameter uncertainty do not change. This makes sense because
the points did not change, so the model should not change. However, our
confidence in the model should change. Chi^2 is an estimate of our confidence
in the model, so it changes while the parameters remain constant
'''

################
# 9
################

r_i = y - y_fit

plt.clf()
plt.errorbar(x, r_i, yerr=y_err, fmt='o')
plt.xlabel('x - data')
plt.ylabel('residuals = y - y_fit')
# plt.savefig('figures/629.png')
# plt.show()

'''
residuals are the difference between the actual data points and our fit model.
I would expect to see points that are both above and below zero - but I would
also zero to be contained in most (~2/3 or more) of the error bars

every point on zero would represent a perfect fit
'''


################
# 10
################

wrongfit = 10.5 * x - 7.2
wrong_r_i = y - wrongfit

plt.clf()
# plt.plot(x, wrongfit)
plt.errorbar(x, wrong_r_i, yerr=y_err, fmt='o')
plt.xlabel('x - data')
plt.ylabel('residuals = y - wrongfit')
# plt.savefig('figures/6210a.png')
# plt.show()

'''
We know something went wrong because the residuals are not clustered around
zero - and, moreover - we can't even see the error bars.

The easiest way to correct this is to re-fit the curve. IE we know that we can
get back to the original distribution by: y = wrong_r_i + wrongfit.

So, first do this, then fit the curve. Then plot the fixed curve's residuals
and see if they make more sense
'''

original_distribution = wrong_r_i + wrongfit

re_popt, re_pcov = curve_fit(func_to_fit, x, original_distribution,
                             sigma=y_err, p0=None)

y_re_fit = func_to_fit(x, *popt)

fixed_r_i = y - y_re_fit



plt.clf()
plt.plot(x, y_re_fit, 'r', label='fixed fit')
plt.errorbar(x, fixed_r_i, yerr=y_err, fmt='o')
plt.xlabel('x - data')
plt.ylabel('fixed residuals')
plt.legend()
# plt.savefig('figures/6210b')
# plt.show()
