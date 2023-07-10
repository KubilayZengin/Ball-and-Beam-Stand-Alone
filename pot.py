import serial
import numpy as np
import matplotlib.pyplot as plt

arduino=serial.Serial('COM22',115200,timeout=1)
plt.close('all')
plt.figure()
plt.ion()
plt.show()
data=np.array([])
i=0
while i<1000:
    a = (arduino.readline())
    a.decode()
    b = float(a[0:4])
    data=np.append(data,b)
    plt.cla()
    plt.plot(data)
    plt.pause(0.01)
    i=i+1