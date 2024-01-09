import array
def get_array_slice(array, i, j):
        return array[i:j]
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time