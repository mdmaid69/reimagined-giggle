import array
def get_string_from_array(array):
        return array.tobytes()
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time