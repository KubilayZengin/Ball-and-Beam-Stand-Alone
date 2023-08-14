class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0

    def calculate(self, setpoint, measured_value):
        # Calculate the error
        error = setpoint - measured_value

        # Calculate the proportional term
        P = self.Kp * error

        # Calculate the integral term
        self.integral += error
        I = self.Ki * self.integral

        # Calculate the derivative term
        derivative = error - self.prev_error
        D = self.Kd * derivative

        # Calculate the total control signal
        control_signal = P + I + D

        # Store the current error as the previous error for the next iteration
        self.prev_error = error

        return control_signal
