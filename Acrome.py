"""
This source code is designed for Ball and Beam system by Acrome Robotics
"""

# Library installation commands given below
import customtkinter  # pip install customtkinter
import serial  # pip install serial
import numpy as np  # pip install numpy
import matplotlib.pyplot as plt  # pip install matplotlib

# Set GUI color # Available parameters "light", "dark", "system"
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Initialize GUI
root = customtkinter.CTk()

# Set dimensions of the GUI
root.geometry("500x750")

# Set the title of the GUI
root.title("Stand Alone GUI")

# Initialize the serial communication between Arduino Mega 2560 and Python
arduino = serial.Serial('COM24', 9600, timeout=1)


# Real time data graph plotting
def start():
    # Add previous data to array
    data = np.array([])
    # Add previous data to array
    data2 = np.array([])
    # Set figure size
    plt.rcParams["figure.figsize"] = (8, 7)
    # Create a subplot with size of 2x1
    plt.subplots(2, 1)

    while True:
        # Read serial data
        a = arduino.readline()
        # Decode the given byte data
        a.decode()
        b = float(a[0:4])
        analog_value = (100 * b) / 5
        data = np.append(data, b)
        data2 = np.append(data2, analog_value)

        plt.subplot(2, 1, 1)
        plt.cla()
        plt.plot(data)
        plt.title("Voltage vs Time")
        plt.ylabel("Voltage (V)")
        plt.pause(0.01)

        plt.subplot(2, 1, 2)
        plt.cla()
        plt.plot(data2)
        plt.title("Position vs Time")
        plt.xlabel("Time")
        plt.ylabel("Position (mm)")
        plt.pause(0.01)


# Stop function
def stop():
    print("Terminating...")
    exit(0)


# Step input function
def step():
    # Check whether the input is empty
    if entry1.get() == "":
        print("Enter a reference value between -200 mm and 200 mm.\n")

    # Set value for amplitude range. For this system, default dimension range is -200-200.
    elif -200 <= int(entry1.get()) <= 200:
        amplitude = entry1.get()
        print("Amplitude value set to:", amplitude, "mm.\n")
    # Print error message if entered value is not in range
    else:
        print("Enter a reference value between -200 mm and 200 mm.\n")


# Sin input function
def sin():
    # Check whether the input is empty
    if entry1.get() == "":
        print("Enter a reference value between -200 mm and 200 mm.")

    # Set value for amplitude range. For this system, default dimension range is -200-200.
    elif -200 <= int(entry1.get()) <= 200:
        amplitude = entry1.get()
        print("Amplitude value set to:", amplitude, "mm.\n")

    # Print error message if entered value is not in range
    else:
        print("Enter a reference value between -200 mm and 200 mm.\n")

    # Check whether the input is empty
    if entry2.get() == "":
        print("Enter a reference value between 1 hertz and 1000 hertz.\n")

    # Set value for frequency range. For this system, default dimension range is **-**.
    elif 1 <= int(entry2.get()) <= 1000:
        frequency = entry2.get()
        print("Frequency value set to:", frequency, "hertz.\n")

    # Print error message if entered value is not in range
    else:
        print("Enter a reference value between 1 hertz and 1000 hertz.\n")


# Initialize frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Set different types of font size
Font_tuple = ("Roboto", 20, "bold")
Font_tuple_2 = ("Roboto", 16)
Font_tuple_3 = ("Roboto", 14)

# All necessary items in the GUI
label = customtkinter.CTkLabel(master=frame, text="Acrome Robotics", font=Font_tuple, text_color="red")
label.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="Ball and Beam ", font=Font_tuple, text_color="white")
label.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="Signal Generator", font=Font_tuple_2, text_color="white")
label.pack(pady=12, padx=10)
label.place(x=130, y=170)

button = customtkinter.CTkButton(master=frame, text="Step", command=step, width=75, height=75)
button.pack(pady=3, padx=3)
button.place(x=50, y=210)

button = customtkinter.CTkButton(master=frame, text="Sin", command=sin, width=75, height=75)
button.pack(pady=12, padx=10)
button.place(x=150, y=210)

button = customtkinter.CTkButton(master=frame, text="Ramp", command=sin, width=75, height=75)
button.pack(pady=12, padx=10)
button.place(x=250, y=210)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Amplitude", font=Font_tuple_3)
entry1.pack(pady=12, padx=10)
entry1.place(x=175, y=300)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Frequency", font=Font_tuple_3)
entry2.pack(pady=12, padx=10)
entry2.place(x=175, y=340)

label = customtkinter.CTkLabel(master=frame, text="Amplitude (mm):", font=Font_tuple_3, text_color="white")
label.pack(pady=12, padx=10)
label.place(x=50, y=300)

label = customtkinter.CTkLabel(master=frame, text="Frequency (hertz):", font=Font_tuple_3, text_color="white")
label.pack(pady=12, padx=10)
label.place(x=50, y=340)

label = customtkinter.CTkLabel(master=frame, text="Control Parameters", font=Font_tuple_2, text_color="white")
label.pack(pady=12, padx=10)
label.place(x=115, y=390)

label = customtkinter.CTkLabel(master=frame, text="Velocity", font=Font_tuple_2, text_color="white")
label.pack(pady=12, padx=10)
label.place(x=80, y=430)

label = customtkinter.CTkLabel(master=frame, text="Position", font=Font_tuple_2, text_color="white")
label.pack(pady=12, padx=10)
label.place(x=245, y=430)

entry4 = customtkinter.CTkEntry(master=frame, placeholder_text="Kp", font=Font_tuple_3)
entry4.pack(pady=12, padx=10)
entry4.place(x=30, y=460)

entry5 = customtkinter.CTkEntry(master=frame, placeholder_text="Ki", font=Font_tuple_3)
entry5.pack(pady=12, padx=10)
entry5.place(x=30, y=500)

entry6 = customtkinter.CTkEntry(master=frame, placeholder_text="Kd", font=Font_tuple_3)
entry6.pack(pady=12, padx=10)
entry6.place(x=30, y=540)

entry7 = customtkinter.CTkEntry(master=frame, placeholder_text="Kp", font=Font_tuple_3)
entry7.pack(pady=12, padx=10)
entry7.place(x=200, y=460)

entry8 = customtkinter.CTkEntry(master=frame, placeholder_text="Ki", font=Font_tuple_3)
entry8.pack(pady=12, padx=10)
entry8.place(x=200, y=500)

entry9 = customtkinter.CTkEntry(master=frame, placeholder_text="Kd", font=Font_tuple_3)
entry9.pack(pady=12, padx=10)
entry9.place(x=200, y=540)

button = customtkinter.CTkButton(master=frame, text="Start", command=start, width=150, height=50, fg_color="green")
button.pack(pady=12, padx=10)
button.place(x=115, y=590)

button = customtkinter.CTkButton(master=frame, text="Stop", command=stop, width=150, height=50, fg_color="red")
button.pack(pady=12, padx=10)
button.place(x=115, y=650)

# Activate the GUI
root.mainloop()
