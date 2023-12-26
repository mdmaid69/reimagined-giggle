import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time