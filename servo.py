import serial
import numpy as np
import matplotlib.pyplot as plt

arduino = serial.Serial('COM22',115200,timeout=1)

plt.close('all')
plt.figure()
plt.ion()
plt.show()
data = np.array([])

while True:
    a = (arduino.readline())
    data = np.append(data,a)

    plt.cla()
    plt.plot(data)
    plt.title("Velocity/Time")
    plt.xlabel("Time")
    plt.ylabel("Servo Velocity")
    plt.pause(0.01)





