import array
def get_array_as_float(array):
        return float(array[0])
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time