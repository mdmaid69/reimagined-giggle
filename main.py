import array
def clear_array(array):
        array *= 0
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time