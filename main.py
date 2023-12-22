import array
def get_array_buffer_info(array):
        return array.buffer_info()
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time