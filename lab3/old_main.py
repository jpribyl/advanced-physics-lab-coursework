import model
import matplotlib.pyplot as plt
from measurement import measurement, query, plot_scope




# squareData = measurement(1)
# squareModel = model.square(5.097)


# squareData.model(
    # 'Single Frequency Square',
    # 'Voltage (dBV)', 
    # 'Frequency (kHz)'
# )
# squareModel.model()


# plt.ylim(-125, 20)
# plt.legend()
# plt.savefig('figures/figure1')
# plt.show()
# plt.clf()




# triangleData = measurement(2)
# triangleModel = model.triangle(5.097)

# triangleData.model(
    # 'Single Frequency Triangle',
    # 'Voltage (dBV)', 
    # 'Frequency (kHz)'
# )
# triangleModel.model()


# plt.ylim(-125, 20)
# plt.legend()
# plt.savefig('figures/figure2')
# plt.show()
# plt.clf()



# sineData = measurement(3)


# sineData.model(
    # 'Single Frequency Sine', 
    # 'Voltage (dBV)', 
    # 'Frequency (kHz)')
# sineModel = model.sine(11.097)
# sineModel.model()

# plt.xlim(0,60)
# plt.legend()
# plt.savefig('figures/figure3')
# plt.show()
# plt.clf()

# # convert to kHz
# x = 1000 * sineModel.measurementXValues

# # convert to Linear scale before fitting
# y = 10 ** (sineModel.measurementYValues / 20)

# yerr = sineModel.measurementYError
# # plt.plot(sineModel.transformX(), sineModel.func())
# # plt.show()

# model.curve_fit(
    # sineModel.func, 
    # x, 
    # y,
    # sigma=yerr)
# sineModel.model()


# summer = measurement(4)
# summerModel = model.sineSum(11.097, 11.097, 2.5, .5)

# summerModel.model()
# summer.model(
    # 'Summer Module With Sines', 
    # 'Voltage (dBV)', 
    # 'Frequency (kHz)')

# plt.legend()
# plt.savefig('figures/figure5')
# # plt.show()

# summer = measurement(5)
# summerModel = model.sineSum(11.097, 11.097, 2.5, .5)

# summerModel.model()
# summer.model(
    # 'Summer Module With Sines', 
    # 'Voltage (dBV)', 
    # 'Frequency (kHz)')

# plt.legend()
# plt.savefig('figures/figure5')
# # plt.show()

# summer = measurement(6)
# summerModel = model.sineSum(11.097, 11.697, 2.5, .5)

# summerModel.model()
# summer.model(
    # 'Summer Module With Sines', 
    # 'Voltage (dBV)', 
    # 'Frequency (kHz)')

# plt.legend()
# plt.savefig('figures/figure6')
# # plt.show()


# summer = measurement(7)
# summerModel = model.sineSum(11.097, 22.697, 2.5, .5)

# summerModel.model()
# summer.model(
    # 'Summer Module With Sines', 
    # 'Voltage (dBV)', 
    # 'Frequency (kHz)')

# plt.legend()
# plt.savefig('figures/figure7')
# # plt.show()
# plt.clf()


# product = measurement(8)
# productModel = model.sineMult(11.097, 31.697, 2.5, .5)

# product.model(
    # 'Multiplier Module With Sines', 
    # 'Voltage (dBV)', 
    # 'Frequency (kHz)')
# productModel.model()

# plt.legend()
# plt.savefig('figures/figure8')
# # plt.show()
# plt.clf()

# product = measurement(9)
# productModel = model.sineMult(25.097, 25.097, 2.5, .5)

# product.model(
    # 'Multiplier Module With Sines', 
    # 'Voltage (dBV)', 
    # 'Frequency (kHz)')
# productModel.model()

# plt.legend()
# plt.savefig('figures/figure9')
# # plt.show()
# plt.clf()


# product = measurement(10)
# productModel = model.sineMult(.207, 25.097, 2.5, .5)

# product.model(
    # 'Multiplier Module With Sines', 
    # 'Voltage (dBV)', 
    # 'Frequency (kHz)')
# productModel.model()

# plt.legend()
# plt.savefig('figures/figure10')
# # plt.show()
# plt.clf()




# lrcSine = measurement(13)
# lrcSine.model(
    # 'Sine Response Through LRC',
    # 'Voltage (dBV)',
    # 'Frequency (kHz)'
# )
# lrcSineModel = model.lrcSine(6)
# lrcSineModel.model()
# plt.ylim(-150,30)
# plt.legend()
# plt.savefig('figures/figure13')
# # plt.show()
# plt.clf()


# lrcSine = measurement(14)
# lrcSine.model(
    # 'Sine Response Through LRC',
    # 'Voltage (dBV)',
    # 'Frequency (kHz)'
# )
# lrcSineModel = model.lrcSine(12)
# lrcSineModel.model()
# plt.ylim(-150,30)
# plt.legend()
# plt.savefig('figures/figure14')
# # plt.show()
# plt.clf()


# lrcSine = measurement(15)
# lrcSine.model(
    # 'Sine Response Through LRC',
    # 'Voltage (dBV)',
    # 'Frequency (kHz)'
# )

# lrcSineModel = model.lrcSine(18)
# lrcSineModel.model()
# plt.ylim(-150,30)
# plt.legend()
# plt.savefig('figures/figure15')
# # plt.show()
# plt.clf()


# lrcSine = measurement(16)
# lrcSine.model(
    # 'Magnitude of Noise Through LRC',
    # 'Voltage (dBV)',
    # 'Frequency (kHz)'
# )
# lrcChirpModel = model.lrcChirp()
# lrcChirpModel.model()

# plt.xlim(0,15)

# plt.legend()
# plt.savefig('figures/figure16')
# # plt.show()
# plt.clf()


# lrcChirpMag = measurement(19)
# lrcChirpMag.model(
    # 'Magnitude of Chirp Through LRC',
    # 'Voltage (dBV)',
    # 'Frequency (kHz)')

# lrcChirpModel = model.lrcChirp()
# lrcChirpModel.model()

# plt.xlim(0,15)
# plt.legend()
# plt.savefig('figures/figure19')
# # plt.show()
# plt.clf()



# measurement(16).model('a','a','a')
# plt.show()


lrcMeas = measurement(16)
lrcMeas.model('LRC Chirp', 'dBV', 'kHz', anAlpha=.5)

a = model.lrcChirpNoise(xvals= lrcMeas.xanvalues, yvals=lrcMeas.yanvalues)
a.model()
plt.legend()
plt.show()










# # lrcmodel.model(plotMag=True)
# # lrcmeas.model('LRC Magnitude', 'Voltage (dBv)', 'Frequency (kHz)')


# # plt.legend()
# # # # plt.show()
# # plt.clf()



# # this goes with measurement 28 on the acoustal cavity chirp
# # plt.clf()
# # measurement.plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0010CH1.CSV')
# # measurement.plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0010CH2.CSV', 100)
# # # plt.show()


# ##########################
# # other data
# ##########################

# # plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0002CH1.CSV')

# # plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0003CH1.CSV')

# # plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0004CH1.CSV')
# # plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0004CH2.CSV')

# # plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0005CH1.CSV')
# # plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0005CH2.CSV')

# # plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0006CH1.CSV')
# # plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0006CH2.CSV')


# # plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0007CH1.CSV')
# # plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0007CH2.CSV')


# # plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0008CH1.CSV')
# # plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0008CH2.CSV')


# # plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0009CH1.CSV')
# # plot_scope('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0009CH2.CSV', 100)




# ##########################
# # MATHEMATICA CODE
# ##########################
# # BodePlot[(1 - (2 Pi w)^2 L A + I 2 Pi w R A)^-1, {w, 1000, 15000}]

# # {magnitude, phase} = 
  # # Cases[Normal@
    # # BodePlot[(1 - (2 Pi w)^2 L A + I 2 Pi w R A)^-1, {w, 1000, 
      # # 15000}], Line[pts_] -> pts, Infinity];
