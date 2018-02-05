import numpy as np
import matplotlib.pyplot as plt

############
# 1
############
m = 2
b = -2
x = np.linspace(-15, 15, 100)
y = m*x + b


# equation of a perpedicular line
m2 = -1/2
y2 = m2*x


plt.plot(x, y, 'o', label='original')
plt.plot(x, y2, label='perp')

plt.legend()


plt.xlim(-15, 15)
plt.ylim(-15, 15)


plt.xlabel('x - label')
plt.ylabel('y - label')
plt.savefig('figures/exercise2')




############
# 3
############

plt.clf()
y = x**2
plt.xlim(-5,5)
plt.plot(x, y)
plt.xlabel('x - label')
plt.ylabel('y - label')
plt.savefig('figures/exercise3')


############
# 4
############

plt.clf()

# original
x0 = 0
y0 = 0
a = 1
original = a*(x - x0)**2 + y0

# x0 is the x-value for the base of the parabola
x0 = 1
y0 = 0
a = 1
change_x0 = a*(x - x0)**2 + y0

# y0 is the y-value for the base of the parabola
x0 = 0
y0 = 1
a = 1
change_y0 = a*(x - x0)**2 + y0

# a is the slope of the parabola's sides
x0 = 0
y0 = 0
a = 2
change_a = a*(x - x0)**2 + y0

plt.xlim(-5,5)
plt.ylim(-5,5)

plt.plot(x, original, '^', label='Original')
plt.plot(x, change_x0, '-', label='Vary x0')
plt.plot(x, change_y0, '.', label='Vary y0', MarkerSize=1)
plt.plot(x, change_a, 'o', label='Vary a')
plt.xlabel('x - label')
plt.ylabel('y - label')

plt.legend()
plt.savefig('figures/exercise4')



############
# 5
############

plt.clf()
x0 = 0
y0 = 0
g = 9.81

# solving the equation for 25 degrees
v0x = 54.3785
v0y = 25.3571

t = np.linspace(0, 5, 50)

y = v0y * t - 1 / 2 * g * t ** 2

x = v0x * t 

# angle is np.arctan( v0y / v0x )
# np.sqrt(v0x ** 2 + v0y ** 2) = 60

plt.xlabel('distance (meters)')
plt.ylabel('height (meters)')
plt.plot(x, y)
plt.legend()
plt.savefig('figures/exercise5')



############
# 6
############


plt.clf()
t = np.linspace(0, 10, 50)

# for 45 degres and |v| = 60
midv0x = 42.4264
midv0y = 42.4264

# a nudge under
lowv0x = 46.45
lowv0y = 37.98

# and a nudge over
hiv0x = 37.98
hiv0y = 46.45


ymid = midv0y * t - 1 / 2 * g * t ** 2
xmid = midv0x * t 


yhi = hiv0y * t - 1 / 2 * g * t ** 2
xhi = hiv0x * t 


ylow = lowv0y * t - 1 / 2 * g * t ** 2
xlow = lowv0x * t 


plt.clf()
plt.plot(xmid, ymid, label='45 Degrees')
plt.plot(xhi, yhi, '^', label='Above 45 Degrees')
plt.plot(xlow, ylow, 'o', label='Below 45 Degrees')
plt.xlabel('distance (meters)')
plt.ylabel('height (meters)')
# plt.ylim(0, 120)
plt.legend()
plt.savefig('figures/exercise6a')
plt.show()


plt.clf()
plt.plot(xmid, ymid)
plt.plot(xhi, yhi, '^')
plt.plot(xlow, ylow, 'o')
plt.xlim(320, 375)
plt.plot(xmid, ymid, label='45 Degrees')
plt.plot(xhi, yhi, '^', label='Above 45 Degrees')
plt.plot(xlow, ylow, 'o', label='Below 45 Degrees')
plt.xlabel('distance (meters)')
plt.ylabel('height (meters)')
plt.legend()
plt.ylim(0, 30)
plt.savefig('figures/exercise6b')
plt.show()



