import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


filename = 'data.csv'

# Stock Python
#data = list(zip(*[[float(x) for x in line.strip().split(',')] for line in open(filename,'r').readlines()[15:]]))
"""
data_pandas = pd.read_csv(filename,skiprows=14,delimiter=',')
plt.plot(data_pandas['Time (s)']*1e3,data_pandas['Channel 1 (V)'],label='Capacitor Voltage')
plt.plot(data_pandas['Time (s)']*1e3,data_pandas['Channel 2 (V)'],label='Schmitt Trigger Output')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage')
plt.title('Voltage V.S. Time')
plt.legend()
plt.show()

"""
data_numpy = np.loadtxt(filename,delimiter=',',skiprows=15).T
plt.plot(data_numpy[0]*1e3,data_numpy[1],label='Capacitor Voltage')
plt.plot(data_numpy[0]*1e3,data_numpy[2],label='Schmitt Trigger Output')

# Frequency
V_threshold = 2.4
REs = np.argwhere((data_numpy[1][1:]>V_threshold) & (data_numpy[1][:-1]<V_threshold))
frequency = 1 / np.average(np.diff(data_numpy[0][REs],axis=0))
plt.plot(data_numpy[0][REs]*1e3,data_numpy[1][REs],'ro',label=f'Rising Edges\nFrequency: {round(frequency)} Hz')


plt.xlabel('Time (ms)')
plt.ylabel('Voltage')
plt.title('Voltage V.S. Time')
plt.legend()
plt.show()