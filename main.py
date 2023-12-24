import array
def get_array_as_bool(array):
        return bool(array)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time