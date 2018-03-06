import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fftpack import fft, rfft

scope_data = pd.read_csv(
    '/home/jp/kod/py/bin/venv/py3/phx444/labs/lab3/data/SineData.CSV'
)

analyzer_data = pd.read_csv(
    '/home/jp/kod/py/bin/venv/py3/phx444/labs/lab3/data/SineDataAnalyzer.csv'
)
analyzer_data.columns = ['freq', 'voltage', 'ignore']

scope_data.columns = \
        ['ignore0', 'ignore1', 'ignore2', 'time', 'voltage', 'ignore3']
# print(scope_data['voltage'])
voltage = scope_data['voltage']
time = scope_data['time']

# plt.plot(time, voltage)
# plt.show()
plot_df = pd.DataFrame()
plot_df['y'] = np.fft.rfft(voltage, norm='ortho')
plot_df['x'] = np.fft.rfftfreq(2499, time[2]-time[1])

plot_df = plot_df[plot_df['y'] > 0]
plot_df = plot_df[plot_df['x'] <= 100000]


# plot_df['y'] = (max(voltage) / np.real(plot_df['y'].max())) * (plot_df['y'])
# plt.plot(plot_df['x'], plot_df['y'])

# Number of sample points
N = 2500
# sample spacing
T = time[2]-time[1]
x = np.linspace(0.0, N*T, N)
y = voltage
yf = fft(y)
print(max(2.52 / max(abs(yf)) * yf))
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
plt.plot(xf, (2.5 / max(abs(yf))) * np.abs(yf[0:N//2]))
plt.yscale('log')

plt.plot(analyzer_data['freq'], 10 ** (analyzer_data['voltage'] / 20))
plt.show()


plot_df = pd.DataFrame()
plot_df['y'] = np.fft.rfft(voltage, norm='ortho')
plot_df['x'] = np.fft.rfftfreq(2499, time[2]-time[1])

plot_df = plot_df[plot_df['y'] > 0]
plot_df = plot_df[plot_df['x'] <= 100000]

plot_df['y'] = 20 * np.log10(plot_df['y'])

plt.plot(plot_df['x'], plot_df['y'])
# plot_df['y'] = 20 * np.log10(plot_df['y'])
plt.plot(analyzer_data['freq'], analyzer_data['voltage'])
# plt.show()
