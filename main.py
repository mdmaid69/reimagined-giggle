import array
def get_array_typecode(array):
        return array.typecode
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time