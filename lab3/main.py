import model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from measurement import measurement, query, plot_scope, plot_an

data = measurement(28)
data.model('Acoustical Cavity Transient Response in Frequency Domain', 'Voltage (dBV)', 'Frequency (kHz)',
           plotSc=False)

# mymodel = model.lrcSquare(.33333, numPoints=10000, sampleSpacing=1/2500)
# mymodel.model(style='-', alpha=.5)

plt.legend()
# plt.axvline(x=6.103, ymax=.88, color='k', linestyle='dashed')
# plt.xticks(list(plt.xticks()[0]) + [6.103])
# plt.ylim(-155,40)
# plt.xlim(0, 10)
plt.show()


# p1=pd.read_csv('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0010CH1.CSV')
# p1.columns = ['no','no2','no3','time','volt', 'no4']


# p2=pd.read_csv('/home/johnny/kod/py/bin/venv/py3/phx444/labs/lab3/data/march1/MarchFirst/F0010CH2.CSV')
# p2.columns = ['no','no2','no3','time','volt', 'no4']

# time = p1['time']
# volt = p1['volt']


# time2 = p2['time']
# volt2 = p2['volt']

# plt.plot(time,volt, label='Input V(t) in Volts')
# plt.plot(time2,100*volt2, label='Output V(t) in Centivolts')
# plt.title('Transient Response of Acoustical Cavity in Time Domain')
# plt.xlabel('Time (s)')
# plt.ylabel('Voltage (Volts and Centivolts)')
# plt.legend()
# plt.show()
plt.clf()
