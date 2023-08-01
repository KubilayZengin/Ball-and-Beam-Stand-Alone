"""
This source code is designed for Ball and Beam system by Acrome Robotics
This source code has written in Python 3.7.4
Author: Kubilay ZENGİN
"""

# Library installation commands given below
import customtkinter  # pip install customtkinter
import serial  # pip install serial
import numpy as np  # pip install numpy
import matplotlib.pyplot as plt  # pip install matplotlib
import serial.tools.list_ports
import time  # pip install python-time
import PID  # PID class
from PIL import Image  # pip install pillow

# Detect all available COMs
com_list = serial.tools.list_ports.comports()
available_coms = []
if len(com_list) == 0:
    available_coms.append("None")
    print("No available COM port detected.")
else:
    for element in com_list:
        available_coms.append(element.device)

# Set different font size types
Font_tuple_1 = ("Roboto", 18)
Font_tuple_2 = ("Roboto", 16)
Font_tuple_3 = ("Roboto", 14)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Initialize arduino object as None
        self.arduino = None
        self.pid_controller = None

        # Configure window
        self.title("Acrome Ball and Beam")
        self.geometry(f"{500}x{800}")
        self.frame = customtkinter.CTkFrame(self)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        # Labels
        self.label_1 = customtkinter.CTkLabel(self.frame, text="",
                                              image=customtkinter.CTkImage(dark_image=Image.open("images/acrome.png"),
                                                                           size=(300, 75)))
        self.label_1.pack(padx=10, pady=12)
        self.label_1.place(x=40, y=10)

        self.label_3 = customtkinter.CTkLabel(self.frame, text="Step", font=Font_tuple_3, text_color="white")
        self.label_3.pack(padx=10, pady=12)
        self.label_3.place(x=75, y=386)

        self.label_4 = customtkinter.CTkLabel(self.frame, text="Sin", font=Font_tuple_3, text_color="white")
        self.label_4.pack(padx=10, pady=12)
        self.label_4.place(x=178, y=386)

        self.label_5 = customtkinter.CTkLabel(self.frame, text="Ramp", font=Font_tuple_3, text_color="white")
        self.label_5.pack(padx=10, pady=12)
        self.label_5.place(x=270, y=386)

        self.label_6 = customtkinter.CTkLabel(self.frame, text="Frequency (Hz):", font=Font_tuple_2, text_color="white")
        self.label_6.pack(padx=10, pady=12)
        self.label_6.place(x=50, y=540)

        self.label_7 = customtkinter.CTkLabel(self.frame, text="Amplitude (mm):", font=Font_tuple_2, text_color="white")
        self.label_7.pack(padx=10, pady=12)
        self.label_7.place(x=50, y=500)

        self.label_8 = customtkinter.CTkLabel(self.frame, text="Position\nControl",
                                              font=Font_tuple_2, text_color="white")
        self.label_8.pack(padx=10, pady=12)
        self.label_8.place(x=60, y=186)

        self.label_9 = customtkinter.CTkLabel(self.frame, text="Velocity\nControl", font=Font_tuple_2,
                                              text_color="white")
        self.label_9.pack(padx=10, pady=12)
        self.label_9.place(x=150, y=186)

        self.label_10 = customtkinter.CTkLabel(self.frame, text="Serial Ports", font=Font_tuple_3,
                                               text_color="white")
        self.label_10.pack(padx=10, pady=12)
        self.label_10.place(x=245, y=205)

        self.label_11 = customtkinter.CTkLabel(self.frame, text="Stop Time", font=Font_tuple_3,
                                               text_color="white")
        self.label_11.pack(padx=10, pady=12)
        self.label_11.place(x=245, y=290)

        # Buttons
        self.button_1 = customtkinter.CTkButton(self.frame, text="", width=75, height=75, fg_color="#C41E3A",
                                                image=customtkinter.CTkImage(dark_image=Image.open("images/step.png"),
                                                                             size=(50, 50)), command=self.step)
        self.button_1.pack(padx=10, pady=12)
        self.button_1.place(x=50, y=410)

        self.button_2 = customtkinter.CTkButton(self.frame, text="", width=75, height=75, fg_color="#C41E3A",
                                                image=customtkinter.CTkImage(dark_image=Image.open("images/sin.png"),
                                                                             size=(50, 50)), command=self.sin)
        self.button_2.pack(padx=10, pady=12)
        self.button_2.place(x=150, y=410)

        self.button_3 = customtkinter.CTkButton(self.frame, text="", width=75, height=75, fg_color="#C41E3A",
                                                image=customtkinter.CTkImage(dark_image=Image.open("images/ramp.png"),
                                                                             size=(50, 50)), command=self.step)
        self.button_3.pack(padx=10, pady=12)
        self.button_3.place(x=250, y=410)

        self.start_button = customtkinter.CTkButton(self.frame, text="", width=1, height=1, fg_color="#2B2B2B",
                                                    bg_color="#2B2B2B", command=self.start, border_width=0,
                                                    image=customtkinter.CTkImage
                                                    (dark_image=Image.open("images/start.png"), size=(120, 90)))
        self.start_button.pack(padx=10, pady=12)
        self.start_button.place(x=130, y=575)

        self.stop_button = customtkinter.CTkButton(self.frame, text="", width=1, height=1, fg_color="#2B2B2B",
                                                   bg_color="#2B2B2B", command=self.stop, border_width=0,
                                                   image=customtkinter.CTkImage
                                                   (dark_image=Image.open("images/stop.png"), size=(120, 90)))
        self.stop_button.pack(padx=10, pady=12)
        self.stop_button.place(x=130, y=670)

        # Entries
        self.entry_1 = customtkinter.CTkEntry(self.frame, placeholder_text="")
        self.entry_1.pack(padx=10, pady=12)
        self.entry_1.place(x=185, y=500)

        self.entry_2 = customtkinter.CTkEntry(self.frame, placeholder_text="")
        self.entry_2.pack(padx=10, pady=12)
        self.entry_2.place(x=185, y=540)

        self.entry_3 = customtkinter.CTkEntry(self.frame, placeholder_text="Kp", width=50, font=Font_tuple_3)
        self.entry_3.pack(padx=10, pady=12)
        self.entry_3.place(x=65, y=240)

        self.entry_4 = customtkinter.CTkEntry(self.frame, placeholder_text="Ki", width=50, font=Font_tuple_3)
        self.entry_4.pack(padx=10, pady=12)
        self.entry_4.place(x=65, y=280)

        self.entry_5 = customtkinter.CTkEntry(self.frame, placeholder_text="Kd", width=50, font=Font_tuple_3)
        self.entry_5.pack(padx=10, pady=12)
        self.entry_5.place(x=65, y=320)

        self.entry_6 = customtkinter.CTkEntry(self.frame, placeholder_text="Kp", width=50, font=Font_tuple_3)
        self.entry_6.pack(padx=10, pady=12)
        self.entry_6.place(x=150, y=240)

        self.entry_7 = customtkinter.CTkEntry(self.frame, placeholder_text="Ki", width=50, font=Font_tuple_3)
        self.entry_7.pack(padx=10, pady=12)
        self.entry_7.place(x=150, y=280)

        self.entry_8 = customtkinter.CTkEntry(self.frame, placeholder_text="Kd", width=50, font=Font_tuple_3)
        self.entry_8.pack(padx=10, pady=12)
        self.entry_8.place(x=150, y=320)

        self.entry_9 = customtkinter.CTkEntry(self.frame, placeholder_text="", width=100, font=Font_tuple_3)
        self.entry_9.pack(padx=10, pady=12)
        self.entry_9.place(x=230, y=320)
        # Option menu
        self.com_port_menu = customtkinter.CTkOptionMenu(self.frame, values=available_coms, command=self.set_com,
                                                         width=80, fg_color="black", text_color="white",
                                                         button_color="#C41E3A", corner_radius=10)
        self.com_port_menu.pack(padx=10, pady=12)
        self.com_port_menu.place(x=240, y=235)

    # Set GUI color function.
    @staticmethod
    def set_gui_color(x, y):
        # Modes: "system" (standard), "dark", "light"
        customtkinter.set_appearance_mode(x)
        # Themes: "blue" (standard), "green", "dark-blue"
        customtkinter.set_default_color_theme(y)

    # Plot starting coordinates function
    @staticmethod
    def set_plot_position(f, x, y):
        # Move figure's upper left corner to pixel (x, y)
        backend = plt.get_backend()
        if backend == 'TkAgg':
            f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
        elif backend == 'WXAgg':
            f.canvas.manager.window.SetPosition((x, y))
        else:
            f.canvas.manager.window.move(x, y)

    # GUI starting coordinates function
    def set_gui_position(self, width=500, height=800):
        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry('%dx%d+%d+%d' % (width, height, x - 400, y - 50))

    # Step input function
    def step(self):
        try:
            if -250 <= int(self.entry_1.get()) <= 250:

                amplitude = self.entry_1.get()
                print("Amplitude value set to:", amplitude, "mm.\n")
            else:
                print("Enter a amplitude value between -200 mm and 200 mm.")

        # Check whether the input is empty
        except ValueError:
            print("Enter a amplitude value between -200 mm and 200 mm.")
        except UnboundLocalError:
            print("Enter a amplitude value between -200 mm and 200 mm.")

    # Sin wave input function
    def sin(self):
        try:
            if -250 <= int(self.entry_1.get()) <= 250:

                amplitude = self.entry_1.get()
                print("Amplitude value set to:", amplitude, "mm.")
            else:
                print("Enter a amplitude value between -200 mm and 200 mm.")

            if 1 <= int(self.entry_2.get()) <= 1000:

                frequency = self.entry_2.get()
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

    # Stop function
    @staticmethod
    def stop():
        print("Program terminated.")
        exit(0)

    def set_com(self, com_port: str):
        # Initialize the serial communication between Arduino and Python.
        try:
            self.arduino = serial.Serial(com_port, 9600, timeout=0.05)
            self.arduino.write(30)
            print("Connected to", com_port)
        except serial.SerialException:
            print("Unable to connect.")

    def set_servo_angle(self, angle):
        # Convert the angle to a string and send it to Arduino
        self.arduino.write(f"{angle}\n".encode())

    # Real time data plotter function
    def start(self):
        # Check whether the PID input is empty
        try:
            kp = float(self.entry_3.get())
            ki = float(self.entry_4.get())
            kd = float(self.entry_5.get())
            # Initialize the PID controller with entered gains
            self.pid_controller = PID.PIDController(kp, ki, kd)
        except ValueError:
            print("Enter any value for PID gains.")
        except UnboundLocalError:
            print("Enter any value for PID gains.")
        except NameError:
            print("Enter any value for PID gains.")
        # Define the set point (desired position)
        # set_point = 50.0
        # Create an empty array for incoming data 
        data = np.array([])
        # Create an empty array for time stamps
        timestamps = np.array([])
        # Set figure size
        plt.rcParams["figure.figsize"] = (8, 7)
        # Create a subplot with size of 1x1
        fig, ax = plt.subplots(1, 1)
        # Call set_plot_position function
        self.set_plot_position(fig, 850, 145)

        try:
            time_selected = int(self.entry_9.get())
            real_time = 0
        except ValueError:
            print("Enter integer value for stop time.")
        k = True
        while k:
            try:
                # Read serial data
                byte_data = self.arduino.readline()
                # Read ball position in terms of mm
                position_data = float(byte_data.decode().strip())
                '''
                # Calculate the control signal using the PID controller and the analog value as the set point
                control_signal = self.pid_controller.calculate(set_point, position_data)
                # Send the control signal to Arduino
                self.set_servo_angle(control_signal)
                '''
                # Append data and timestamp to arrays
                data = np.append(data, position_data)
                timestamps = np.append(timestamps, time.time())  # Add the current time as the x-coordinate

                if time_selected <= int(real_time):
                    k = False

                else:
                    # Calculate real-time seconds for each data point
                    realtime = timestamps - timestamps[0]
                    real_time = realtime[-1]
                    plt.cla()
                    plt.grid()
                    plt.ylim(0, 90)
                    plt.plot(realtime, data, color="red")
                    plt.title("Ball Position vs Real Time")
                    plt.ylabel("Position (mm)")
                    plt.xlabel("Time (s)")
                    plt.pause(0.01)

            except KeyboardInterrupt:
                # If the user presses Ctrl+F2 or manually stops, terminate the program.
                print("Program terminated.")
            except AttributeError:
                print("Select your COM Port.")
                plt.close()
                break
            except serial.SerialException:
                # Handle SerialException error when opening the port
                print("Error: Unable to open the serial port. \n"
                      "Check the port number and connection or restart the program.")
            except ValueError:
                # If ValueError occurs, continue to the next iteration to read the next line.
                continue
            except NameError:
                break


if __name__ == "__main__":
    try:
        app = App()
        app.set_gui_color("dark", "dark-blue")
        app.set_gui_position()
        app.mainloop()
    except KeyboardInterrupt:
        # If the user presses Ctrl+F2 or manually stops, terminate the program.
        print("Program terminated.")
