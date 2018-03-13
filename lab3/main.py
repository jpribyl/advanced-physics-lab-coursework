import model
import numpy as np
import matplotlib.pyplot as plt
from measurement import measurement, query, plot_scope, plot_an

data = measurement(5)
data.model('LRC Transient Response', 'Voltage (dB)', 'Frequency (kHz)',
           plotSc=False)

mymodel = model.sineSum(11.097, 11.597, 5,1)
mymodel.model()

plt.legend()
# plt.axvline(x=6.103, ymax=.88, color='k', linestyle='dashed')
# plt.xticks(list(plt.xticks()[0]) + [6.103])
# plt.ylim(-150,50)
# plt.xlim(1, 25)
plt.show()
plt.clf()
