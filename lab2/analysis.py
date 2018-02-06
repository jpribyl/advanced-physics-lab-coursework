import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.umath import *
from uncertainties import unumpy
from uncertainties.unumpy import uarray

################################
# FIRST DEFINE GLOBAL CONSTANTS
################################
g = 9.81
mu0 = 1.25663706 * 10**(-6)


################################
# IMPORT DATA TO NP & PD
################################

'''
# into np
with open('data/magnetic.csv') as file:
    np_data = np.genfromtxt(file, delimiter=',')
'''



# into pandas
xl = pd.ExcelFile('data/magnetic.xlsx')
df =xl.parse('Sheet1')


################################
# MAGNETIC FIELD DATA
################################

b_cal_length = 10.00 / 1000

# magnet masses from calibration with and without the current turned on
# you can apply the error with a lambda function or uarray (see a few lines down)
b_cal_scale_no_current = df['scale_no_mag_si'].dropna().apply(lambda x: ufloat(x, .00001))
b_cal_scale_with_current = df['scale_with_mag_si'].dropna().apply(lambda x: ufloat(x, .00001))



# current error according to the manufacturer's specs
current_error = 1000 * df['current'].dropna() * 10 ** -6 + 3 * 15 * 10**-6

# currents used during calibration
# this method returns a np array, so I convert it back into a pd element
b_cal_current = pd.Series(uarray(df['current'].dropna(), current_error))

b_cal_mass_difference = b_cal_scale_no_current - b_cal_scale_with_current
# print(b_cal_mass_difference)


################################
# MAGNETIC FIELD EQUATION
################################

# define the magnetic field as in lecture
def mag_field(mass, current, length):
    return (mass * g) / (current * length)


bcal = mag_field(b_cal_mass_difference, b_cal_current, b_cal_length)

################################
# MAGNETIC FIELD FUNCTION FIT
################################

# separate the values and error
b_cal_values = bcal.apply(lambda x: x.n)
b_cal_error = bcal.apply(lambda x: x.s)

# same thing for the current
current_values = b_cal_current.apply(lambda x: x.n)


def lin_fit(x, a, b):
    return a*x + b


# propagating error for model fits is outside the scope of this course
popt, pcov = curve_fit(lin_fit, current_values, b_cal_values)
b_fit = lin_fit(current_values, *popt)


################################
# PLOT THE RESULTS
################################
plt.errorbar(current_values,
             b_cal_values,
             yerr=b_cal_error,
             fmt='o',
             label='B Data')

plt.plot(current_values, b_fit, label='B Fit')
plt.ylim(.4, .43)
plt.legend()
plt.savefig('figures/figure1.png')
plt.xlabel('Current Value (A)')
plt.ylabel('Residuals (T)')
plt.show()

r_i = b_cal_values - b_fit
plt.clf()
plt.errorbar(
    current_values,
    r_i,
    yerr=b_cal_error,
    fmt='o')
plt.xlabel('Current Value (A)')
plt.ylabel('Residuals (T)')
plt.show()


################################
# Xm DATA
################################

# let's go ahead and condense the b field down to a single point
bcal = bcal.sum() / len(bcal)

# strip whitespace off sample names
name = df['sample_name'].str.strip()

# density values are literature and have ~0 uncertainty
density = df['density_kg_m']
lit_xm = df['lit_xm']

# propagating uncertainty for all data we collected
area = \
        df['area_param_1'].apply(lambda x: ufloat(x, .0001)) * \
        df['area_param_2'].apply(lambda x: ufloat(x, .0001))


'''
the area uncertainty for cobalt is very close to zero, and we are given the
dimesions of the cobalt wire - so I will assume that the dimensions we are
given are exact. Without this assumption, it's really easy to hit an error bar
of 80,000
'''
area[4] = area[4].n

height = df['height_sample'].apply(lambda x: ufloat(x, .0001))
real_mass = df['sample_mass_si'].apply(lambda x: ufloat(x, .000001))
volume = area * height
theory_mass = volume * density

# ensure that there are no percentages over 100 without dropping uncertainties
percent_real = (real_mass / theory_mass).apply(lambda x: ufloat(min(x.n, 1), x.s))

# update area so that it represents the actual area occupied by the substance
area = area * percent_real


no_sample_magnet_mass = df['scale_mass_si'].apply(lambda x: ufloat(x, .000001))
sample_magnet_mass = df['sample_magnet_si'].apply(lambda x: ufloat(x, .000001))
sample_mass_difference = no_sample_magnet_mass - sample_magnet_mass


################################
# Xm FUNCTION
################################
def xm(mass_difference, area):
    return (2 * mu0 * mass_difference * g) / (area * bcal**2)


sample_xm = xm(sample_mass_difference, area)
sample_xm_values = sample_xm.apply(lambda x: x.n)
sample_xm_err = sample_xm.apply(lambda x: x.s)

################################
# PLOTTING DATA
################################
plt.clf()

plt.bar(name[0:4], sample_xm_values[0:4], yerr=sample_xm_err[0:4],
        label='Data', alpha=.5)

plt.bar(name[0:4], lit_xm[0:4], label=' Lit Value (If Exists)', alpha=.4)
plt.ylabel('Volume X_m in SI')
plt.legend()
plt.savefig('figures/figure2')
plt.show()

plt.clf()
plt.bar(name[[5,6,9,10,11]], sample_xm_values[[5,6,9,10,11]],
        yerr=sample_xm_err[[5,6,9,10,11]], alpha=.5, label='Data')

plt.bar(name[[5,6,9,10,11]], lit_xm[[5,6,9,10,11]], label=' Lit Value (If Exists)', alpha=.4)
plt.ylabel('Volume X_m in SI')
plt.legend()
plt.savefig('figures/figure3')
plt.show()

plt.clf()
plt.bar(name[[7,8,13,14]], sample_xm_values[[7,8,13,14]],
        yerr=sample_xm_err[[7,8,13,14]],label='Data')
plt.bar(name[[7,8,13,14]], lit_xm[[7,8,13,14]], label=' Lit Value (If Exists)', alpha=.4)
plt.ylabel('Volume X_m in SI')
plt.legend()
plt.savefig('figures/figure4')
plt.show()

plt.clf()
plt.bar(name[[15,17]], sample_xm_values[[15,17]],
        yerr=sample_xm_err[[15,17]], label='Data')

plt.bar(name[[15,17]], lit_xm[[15,17]], label=' Lit Value (If Exists)', alpha=.4)
plt.ylabel('Volume X_m in SI')
plt.legend()
plt.savefig('figures/figure5')
plt.show()


plt.clf()
plt.bar(name[[12,16,18]], sample_xm_values[[12,16,18]],
        yerr=sample_xm_err[[12,16,18]], label='Data')

plt.bar(name[[12,16,18]], lit_xm[[12,16,18]], label=' Lit Value (If Exists)', alpha=.4)
plt.ylabel('Volume X_m in SI')
plt.legend()
plt.savefig('figures/figure6')
plt.show()

plt.clf()
plt.bar(name[[4]], sample_xm_values[[4]], yerr=sample_xm_err[[4]], label='Data')
plt.bar(name[[4]], lit_xm[[4]], label=' Lit Value (If Exists)', alpha=.4)
plt.ylabel('Volume X_m in SI')
plt.legend()
plt.savefig('figures/figure7')
plt.show()


plt.clf()
plt.errorbar(lit_xm, sample_xm_values, fmt='.', yerr=sample_xm_err)
plt.xlabel('Literature X_m')
plt.ylabel('Measured X_m')
plt.savefig('figures/figure8')
plt.show()
