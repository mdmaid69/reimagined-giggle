import array
def get_array_buffer_info(array):
        return array.buffer_info()
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)