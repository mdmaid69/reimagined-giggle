import sys
def exit_program():
        sys.exit()
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time