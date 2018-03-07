import model
import matplotlib.pyplot as plt
from measurement import measurement, query, plot_scope

data = measurement(1)
mymodel = model.square(5097)

data.model('Square Wave', 'Voltage (dB and dBV)', 'Frequency (kHz)')
mymodel.model()

plt.legend()
plt.ylim(-100,50)
plt.show()
plt.clf()
