import model
import numpy as np
import matplotlib.pyplot as plt
from measurement import measurement, query, plot_scope, plot_an

data = measurement(15)
mymodel = model.lrcSine(18)

data.model('Sine Wave Data With a Model', 'Voltage (dB)', 'Frequency (kHz)')
mymodel.model()

plt.legend()
plt.ylim(-130,50)
plt.xlim(0,40)
plt.show()
plt.clf()

