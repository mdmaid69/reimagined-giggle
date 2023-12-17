import array
def get_array_as_bytes(array):
        return bytes(array)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time