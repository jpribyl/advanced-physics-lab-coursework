import model
import matplotlib.pyplot as plt
from measurement import measurement, query, plot_scope



squareData = measurement(1)
squareModel = model.square(5.097)


squareData.model(
    'Single Frequency Square',
    'Voltage (dBV)', 
    'Frequency (kHz)'
)
squareModel.model()


plt.ylim(-125, 20)
plt.legend()
# plt.show()
plt.clf()




triangleData = measurement(2)
triangleModel = model.triangle(5.097)

triangleData.model(
    'Single Frequency Triangle',
    'Voltage (dBV)', 
    'Frequency (kHz)'
)
triangleModel.model()


plt.ylim(-125, 20)
plt.legend()
# plt.show()
plt.clf()



sineData = measurement(3)
sineModel = model.sine(11.097)


sineData.model(
    'Single Frequency Sine', 
    'Voltage (dBV)', 
    'Frequency (kHz)')
sineModel.model()


plt.xlim(0,60)
plt.legend()
# plt.show()
plt.clf()

summer = measurement(4)
summerModel = model.sineSum(11.097, 11.097, 2.5, .5)

summerModel.model()
summer.model(
    'Summer Module With Sines', 
    'Voltage (dBV)', 
    'Frequency (kHz)')

plt.legend()
# plt.show()

summer = measurement(5)
summerModel = model.sineSum(11.097, 11.097, 2.5, .5)

summerModel.model()
summer.model(
    'Summer Module With Sines', 
    'Voltage (dBV)', 
    'Frequency (kHz)')

plt.legend()
# plt.show()

summer = measurement(6)
summerModel = model.sineSum(11.097, 11.697, 2.5, .5)

summerModel.model()
summer.model(
    'Summer Module With Sines', 
    'Voltage (dBV)', 
    'Frequency (kHz)')

plt.legend()
# plt.show()


summer = measurement(7)
summerModel = model.sineSum(11.097, 22.697, 2.5, .5)

summerModel.model()
summer.model(
    'Summer Module With Sines', 
    'Voltage (dBV)', 
    'Frequency (kHz)')

# plt.legend()
# plt.show()
plt.clf()


product = measurement(8)
productModel = model.sineMult(11.097, 31.697, 2.5, .5)

product.model(
    'Multiplier Module With Sines', 
    'Voltage (dBV)', 
    'Frequency (kHz)')
productModel.model()

plt.legend()
# plt.show()
plt.clf()

product = measurement(9)
productModel = model.sineMult(25.097, 25.097, 2.5, .5)

product.model(
    'Multiplier Module With Sines', 
    'Voltage (dBV)', 
    'Frequency (kHz)')
productModel.model()

plt.legend()
# plt.show()
plt.clf()


product = measurement(10)
productModel = model.sineMult(.207, 25.097, 2.5, .5)

product.model(
    'Multiplier Module With Sines', 
    'Voltage (dBV)', 
    'Frequency (kHz)')
productModel.model()

plt.legend()
# plt.show()
# lrcmeas = measurement(19)
# lrcmodeSil = model.lrc()


# lrcmodel.model(plotMag=True)
# lrcmeas.model('LRC Magnitude', 'Voltage (dBv)', 'Frequency (kHz)')


# plt.legend()
# # plt.show()
# plt.clf()



# this goes with measurement 28 on the acoustal cavity chirp
# plt.clf()
# measurement.plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0010CH1.CSV')
# measurement.plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0010CH2.CSV', 100)
# plt.show()


##########################
# other data
##########################

# plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0002CH1.CSV')

# plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0003CH1.CSV')

# plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0004CH1.CSV')
# plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0004CH2.CSV')

# plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0005CH1.CSV')
# plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0005CH2.CSV')

# plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0006CH1.CSV')
# plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0006CH2.CSV')


# plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0007CH1.CSV')
# plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0007CH2.CSV')


# plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0008CH1.CSV')
# plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0008CH2.CSV')


# plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0009CH1.CSV')
# plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0009CH2.CSV', 100)




##########################
# MATHEMATICA CODE
##########################
# BodePlot[(1 - (2 Pi w)^2 L A + I 2 Pi w R A)^-1, {w, 1000, 15000}]

# {magnitude, phase} = 
  # Cases[Normal@
    # BodePlot[(1 - (2 Pi w)^2 L A + I 2 Pi w R A)^-1, {w, 1000, 
      # 15000}], Line[pts_] -> pts, Infinity];
