import array
def get_array_slice(array, i, j):
        return array[i:j]
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time