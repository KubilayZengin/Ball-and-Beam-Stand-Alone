import customtkinter
import serial
import numpy as np
import matplotlib.pyplot as plt

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("350x700")
root.title("Stand Alone GUI")

arduino = serial.Serial('COM3', 115200, timeout=1)

def voltage():
    print("Graph is live")
    data = np.array([])

    while True:
        a = arduino.readline()
        a.decode()
        b = float(a[0:4])
        data = np.append(data, b)

        plt.cla()
        plt.plot(data)
        plt.title("Voltage/Time")
        plt.xlabel("Time")
        plt.ylabel("Voltage")
        plt.pause(0.01)

def position():
    print("Graph is live")
    data = np.array([])

    while True:
        a = arduino.readline()
        a.decode()
        b = float(a[0:4])
        analog_value = (1024 * b) / 5
        data = np.append(data, analog_value)

        plt.cla()
        plt.plot(data)
        plt.title("Position/Time")
        plt.xlabel("Time")
        plt.ylabel("Analog Value")
        plt.pause(0.01)

def stop():
    print("Terminating...")
    exit(0)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Ball and Beam GUI", font=("Inter", 24))
label.pack(pady=12,padx=10)

label = customtkinter.CTkLabel(master=frame, text="Scopes", font=("Inter", 16))
label.pack(pady=12,padx=10)
label.place(x=85,y=40)

label = customtkinter.CTkLabel(master=frame, text="Position (rad)", font=("Arial", 12))
label.pack(pady=12,padx=10)
label.place(x=30,y=70)

label = customtkinter.CTkLabel(master=frame, text="Current (A)", font=("Arial", 12))
label.pack(pady=12,padx=10)
label.place(x=30,y=90)

label = customtkinter.CTkLabel(master=frame, text="Voltage (V)", font=("Arial", 12))
label.pack(pady=12,padx=10)
label.place(x=30,y=110)

label = customtkinter.CTkLabel(master=frame, text="Signal Generator", font=("Arial", 16))
label.pack(pady=12,padx=10)
label.place(x=60,y=145)

label = customtkinter.CTkLabel(master=frame, text="Step", font=("Arial", 12))
label.pack(pady=12,padx=10)
label.place(x=37,y=180)

button= customtkinter.CTkButton(master=frame,text="Step",command=stop,width=50,height=50)
button.pack(pady=3,padx=3)
button.place(x=30,y=210)

label = customtkinter.CTkLabel(master=frame, text="Sin", font=("Arial", 12))
label.pack(pady=12,padx=10)
label.place(x=105,y=180)

button= customtkinter.CTkButton(master=frame,text="Sin",command=stop,width=50,height=50)
button.pack(pady=12,padx=10)
button.place(x=90,y=210)

label = customtkinter.CTkLabel(master=frame, text="Ramp", font=("Arial", 12))
label.pack(pady=12,padx=10)
label.place(x=165,y=180)

button= customtkinter.CTkButton(master=frame,text="Ramp",command=stop,width=50,height=50)
button.pack(pady=12,padx=10)
button.place(x=150,y=210)

entry1= customtkinter.CTkEntry(master=frame, placeholder_text="Amplitude")
entry1.pack(pady=12,padx=10)
entry1.place(x=30,y=280)

entry1= customtkinter.CTkEntry(master=frame, placeholder_text="Frequency")
entry1.pack(pady=12,padx=10)
entry1.place(x=30,y=320)

entry1= customtkinter.CTkEntry(master=frame, placeholder_text="Offset")
entry1.pack(pady=12,padx=10)
entry1.place(x=30,y=360)

label = customtkinter.CTkLabel(master=frame, text="Control Parameters", font=("Arial", 16))
label.pack(pady=12,padx=10)
label.place(x=55,y=400)

entry1= customtkinter.CTkEntry(master=frame, placeholder_text="Kp")
entry1.pack(pady=12,padx=10)
entry1.place(x=30,y=435)

entry2= customtkinter.CTkEntry(master=frame, placeholder_text="Ki")
entry2.pack(pady=12,padx=10)
entry2.place(x=30,y=475)

entry3= customtkinter.CTkEntry(master=frame, placeholder_text="Kd")
entry3.pack(pady=12,padx=10)
entry3.place(x=30,y=515)

button= customtkinter.CTkButton(master=frame,text="Voltage/Time Graph",command=voltage)
button.pack(pady=12,padx=10)
button.place(x=30,y=560)

button= customtkinter.CTkButton(master=frame,text="Position/Time Graph",command=position)
button.pack(pady=12,padx=10)
button.place(x=30,y=590)

button= customtkinter.CTkButton(master=frame,text="Stop",command=stop)
button.pack(pady=12,padx=10)
button.place(x=30,y=620)

root.mainloop()
