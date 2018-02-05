import numpy as np
import matplotlib.pyplot as plt


############
# 6
############


t = np.linspace(0, 10, 50)
g = 9.8

# for 45 degres and |v| = 60
midv0x = 42.4264
midv0y = 42.4264

# a nudge under
lowv0x = 46.45
lowv0y = 37.98

# and a nudge over
hiv0x = 37.98
hiv0y = 46.45


ymid = midv0y * t - 1/2*g*t**2
xmid = midv0x * t 


yhi = hiv0y * t - 1 / 2 * g * t ** 2
xhi = hiv0x * t 


ylow = lowv0y * t - 1 / 2 * g * t ** 2
xlow = lowv0x * t 

y = midv0y*t-1/2 * g*t**2
x=midv0x*t
plt.plot(x, y)
plt.plot(xmid, ymid)
plt.show()

# plt.plot(xmid, ymid, label='45 Degrees')
# plt.plot(xhi, yhi, '^', label='Above 45 Degrees')
# plt.plot(xlow, ylow, 'o', label='Below 45 Degrees')
# plt.xlabel('distance (meters)')
# plt.ylabel('height (meters)')
# # plt.ylim(0, 120)
# plt.legend()
# plt.savefig('figures/exercise6a')
# plt.show()


# plt.clf()
# plt.plot(xmid, ymid)
# plt.plot(xhi, yhi, '^')
# plt.plot(xlow, ylow, 'o')
# plt.xlim(320, 375)
# plt.plot(xmid, ymid, label='45 Degrees')
# plt.plot(xhi, yhi, '^', label='Above 45 Degrees')
# plt.plot(xlow, ylow, 'o', label='Below 45 Degrees')
# plt.xlabel('distance (meters)')
# plt.ylabel('height (meters)')
# plt.legend()
# plt.ylim(0, 30)
# plt.savefig('figures/exercise6b')
# # plt.show()



