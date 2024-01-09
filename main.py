import array
def convert_array_to_bytes(array):
        return array.tobytes()
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time