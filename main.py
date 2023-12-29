import array
def get_array_buffer_info(array):
        return array.buffer_info()
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time