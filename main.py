import array
def convert_array_to_bytes(array):
        return array.tobytes()
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time