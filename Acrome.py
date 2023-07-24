"""
This source code is designed for Ball and Beam system by Acrome Robotics
Author: Kubilay ZENGİN
"""
# Library installation commands given below
import customtkinter  # pip install customtkinter
import serial  # pip install serial
import numpy as np  # pip install numpy
import matplotlib.pyplot as plt  # pip install matplotlib
from PIL import Image  # pip install pillow
import PID  # PID class


# GUI start coordinates function
def set_gui_position(width=500, height=800):
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x - 400, y - 50))


# Plot start coordinates function
def set_plot_position(f, x, y):
    # Move figure's upper left corner to pixel (x, y)
    backend = plt.get_backend()
    if backend == 'TkAgg':
        f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
    elif backend == 'WXAgg':
        f.canvas.manager.window.SetPosition((x, y))
    else:
        f.canvas.manager.window.move(x, y)


# Set GUI color function.
def set_gui_color(x, y):
    # Available parameters for x: "light", "dark", "system".
    customtkinter.set_appearance_mode(x)
    # Available parameters for y: "blue", "green", "dark-blue".
    customtkinter.set_default_color_theme(y)


def set_servo_angle(angle):
    # Convert the angle to a string and send it to Arduino
    arduino.write(f"{angle}\n".encode())


# Stop function
def stop():
    print("Program terminated.")
    exit(0)


# Step input function
def step():
    try:
        if -200 <= int(entry1.get()) <= 200:

            amplitude = entry1.get()
            print("Amplitude value set to:", amplitude, "mm.\n")
        else:
            print("Enter a amplitude value between -200 mm and 200 mm.")

    # Check whether the input is empty
    except ValueError:
        print("Enter a amplitude value between -200 mm and 200 mm.")
    except UnboundLocalError:
        print("Enter a amplitude value between -200 mm and 200 mm.")


# Sin wave input function
def sin():
    try:
        if -200 <= int(entry1.get()) <= 200:

            amplitude = entry1.get()
            print("Amplitude value set to:", amplitude, "mm.")
        else:
            print("Enter a amplitude value between -200 mm and 200 mm.")

        if 1 <= int(entry2.get()) <= 1000:

            frequency = entry2.get()
            print("Frequency value set to:", frequency, "hertz.\n")
        else:
            print("Enter a frequency value between 1 hertz and 1000 hertz.\n")

    # Check whether the input is empty
    except ValueError:
        print("Enter a amplitude value between -200 mm and 200 mm.")
        print("Enter a frequency value between 1 hertz and 1000 hertz.\n")
    except UnboundLocalError:
        print("Enter a amplitude value between -200 mm and 200 mm.")
        print("Enter a frequency value between 1 hertz and 1000 hertz.\n")


try:
    # Initialize the serial communication between Arduino Mega 2560 and Python.
    arduino = serial.Serial('COM24', 9600, timeout=1)
except serial.SerialException:
    # Handle SerialException error when opening the port
    print("No arduino detected.")


# Real time data plotter function
def start():
    # noinspection PyGlobalUndefined
    global pid_controller
    # Check whether the PID input is empty
    try:
        kp = float(entry3.get())
        ki = float(entry4.get())
        kd = float(entry5.get())
        # Initialize the PID controller with appropriate gains
        pid_controller = PID.PIDController(kp, ki, kd)
    except ValueError:
        print("Enter any value for PID gains.")
    except UnboundLocalError:
        print("Enter any value for PID gains.")
    except NameError:
        print("Enter any value for PID gains.")
    # Define the set point (desired position)
    set_point = 50.0

    # Create an empty array
    data = np.array([])
    # Set figure size
    plt.rcParams["figure.figsize"] = (8, 7)
    # Create a subplot with size of 2x1
    fig, ax = plt.subplots(1, 1)
    # Call set_plot_position function
    set_plot_position(fig, 850, 145)
    while True:
        try:
            # Read serial data
            byte_data = arduino.readline()
            # Decode byte data
            byte_data.decode()
            # Ball position in terms of mm
            position_data = float(byte_data[0:4])
            data = np.append(data, position_data)
            # Calculate the control signal using the PID controller and the analog value as the set point
            control_signal = pid_controller.calculate(set_point, position_data)
            print("Position  data: ", position_data)
            print("Control signal: ", control_signal)

            # Send the control signal to Arduino
            set_servo_angle(control_signal)

            plt.cla()
            plt.grid()
            plt.plot(data)
            plt.title("Ball Position vs Sample rate")
            plt.ylabel("Position (mm)")
            plt.xlabel("Sample (n)")
            plt.pause(0.01)

        except KeyboardInterrupt:
            # If the user presses Ctrl+F2, stop the program
            print("Program terminated.")
        except serial.SerialException:
            # Handle SerialException error when opening the port
            print("Error: Unable to open the serial port. Check the port number and connection or restart the program.")
        except ValueError:
            # If there's an issue converting data to the appropriate format, handle the error here
            print("Error: Unable to convert data.")
            plt.clf()
        except NameError:
            # If there's an issue converting data to the appropriate format, handle the error here
            break


try:
    # Call set GUI color function
    set_gui_color("dark", "dark-blue")
    # Initialize GUI
    root = customtkinter.CTk()
    # Set the dimensions of the GUI
    root.geometry("500x800")
    # Set the title of the GUI
    root.title("Acrome Ball and Beam")
    # Initialize frame
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    # Set different font size types
    Font_tuple = ("Roboto", 25, "bold")
    Font_tuple_2 = ("Roboto", 16)
    Font_tuple_3 = ("Roboto", 14)
    Font_tuple_4 = ("Roboto", 10)

    # GUI visual attributes
    acrome_png = customtkinter.CTkImage(dark_image=Image.open("images/acrome.png"), size=(300, 75))
    step_png = customtkinter.CTkImage(dark_image=Image.open("images/step.png"), size=(50, 50))
    sin_png = customtkinter.CTkImage(dark_image=Image.open("images/sin.png"), size=(50, 50))
    ramp_png = customtkinter.CTkImage(dark_image=Image.open("images/ramp.png"), size=(50, 50))
    start_png = customtkinter.CTkImage(dark_image=Image.open("images/start.png"), size=(70, 55))
    stop_png = customtkinter.CTkImage(dark_image=Image.open("images/stop.png"), size=(70, 55))

    label = customtkinter.CTkLabel(master=frame,
                                   text="",
                                   image=acrome_png)
    label.pack(pady=12, padx=10)
    label.place(x=30, y=10)

    label = customtkinter.CTkLabel(master=frame,
                                   text="Ball and Beam ",
                                   font=Font_tuple,
                                   text_color="white")
    label.pack(pady=12, padx=10)
    label.place(x=110, y=115)

    label = customtkinter.CTkLabel(master=frame,
                                   text="Step",
                                   font=Font_tuple_3,
                                   text_color="white")
    label.pack(pady=12, padx=10)
    label.place(x=75, y=186)

    label = customtkinter.CTkLabel(master=frame,
                                   text="Sin",
                                   font=Font_tuple_3,
                                   text_color="white")
    label.pack(pady=12, padx=10)
    label.place(x=180, y=186)

    label = customtkinter.CTkLabel(master=frame,
                                   text="Ramp",
                                   font=Font_tuple_3,
                                   text_color="white")
    label.pack(pady=12, padx=10)
    label.place(x=267, y=186)

    button = customtkinter.CTkButton(master=frame,
                                     text="",
                                     image=step_png,
                                     command=step,
                                     width=75,
                                     height=75,
                                     fg_color="white")
    button.pack(pady=12, padx=10)
    button.place(x=50, y=210)

    button = customtkinter.CTkButton(master=frame,
                                     text="",
                                     image=sin_png,
                                     command=sin,
                                     width=75,
                                     height=75,
                                     fg_color="white")
    button.pack(pady=12, padx=10)
    button.place(x=150, y=210)

    button = customtkinter.CTkButton(master=frame,
                                     text="",
                                     text_color="black",
                                     image=ramp_png,
                                     width=75,
                                     height=75,
                                     fg_color="white")
    button.pack(pady=12, padx=10)
    button.place(x=250, y=210)

    entry1 = customtkinter.CTkEntry(master=frame,
                                    placeholder_text="")
    entry1.pack(pady=12, padx=10)
    entry1.place(x=185, y=300)

    entry2 = customtkinter.CTkEntry(master=frame,
                                    placeholder_text="")
    entry2.pack(pady=12, padx=10)
    entry2.place(x=185, y=340)

    label = customtkinter.CTkLabel(master=frame,
                                   text="Amplitude (mm):",
                                   font=Font_tuple_2,
                                   text_color="white")
    label.pack(pady=12, padx=10)
    label.place(x=50, y=300)

    label = customtkinter.CTkLabel(master=frame,
                                   text="Frequency (Hz):",
                                   font=Font_tuple_2,
                                   text_color="white")
    label.pack(pady=12, padx=10)
    label.place(x=50, y=340)

    label = customtkinter.CTkLabel(master=frame,
                                   text="Position\nControl",
                                   font=Font_tuple_2,
                                   text_color="white")
    label.pack(pady=12, padx=10)
    label.place(x=110, y=410)

    label = customtkinter.CTkLabel(master=frame,
                                   text="Velocity\nControl",
                                   font=Font_tuple_2,
                                   text_color="white")
    label.pack(pady=12, padx=10)
    label.place(x=215, y=410)

    entry3 = customtkinter.CTkEntry(master=frame,
                                    placeholder_text="Kp",
                                    width=80,
                                    font=Font_tuple_3)
    entry3.pack(pady=12, padx=10)
    entry3.place(x=100, y=460)

    entry4 = customtkinter.CTkEntry(master=frame,
                                    placeholder_text="Ki",
                                    width=80,
                                    font=Font_tuple_3)
    entry4.pack(pady=12, padx=10)
    entry4.place(x=100, y=500)

    entry5 = customtkinter.CTkEntry(master=frame,
                                    placeholder_text="Kd",
                                    width=80,
                                    font=Font_tuple_3)
    entry5.pack(pady=12, padx=10)
    entry5.place(x=100, y=540)

    entry = customtkinter.CTkEntry(master=frame,
                                   placeholder_text="Kp",
                                   width=80,
                                   font=Font_tuple_3)
    entry.pack(pady=12, padx=10)
    entry.place(x=200, y=460)

    entry = customtkinter.CTkEntry(master=frame,
                                   placeholder_text="Ki",
                                   width=80,
                                   font=Font_tuple_3)
    entry.pack(pady=12, padx=10)
    entry.place(x=200, y=500)

    entry = customtkinter.CTkEntry(master=frame,
                                   placeholder_text="Kd",
                                   width=80,
                                   font=Font_tuple_3)
    entry.pack(pady=12, padx=10)
    entry.place(x=200, y=540)

    button = customtkinter.CTkButton(master=frame,
                                     text="",
                                     image=start_png,
                                     command=start,
                                     width=80,
                                     height=60,
                                     fg_color="green",
                                     corner_radius=100)
    button.pack(pady=12, padx=10)
    button.place(x=116, y=600)

    button = customtkinter.CTkButton(master=frame,
                                     text="",
                                     image=stop_png,
                                     command=stop,
                                     width=80,
                                     height=60,
                                     fg_color="red",
                                     corner_radius=100)
    button.pack(pady=12, padx=10)
    button.place(x=116, y=680)

    # Call set_gui_position()
    set_gui_position()
    # Activate the GUI
    root.mainloop()

except KeyboardInterrupt:
    # If the user presses Ctrl+F2, stop the program
    print("Program terminated.")
