import array
def get_array_buffer_info(array):
        return array.buffer_info()
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time