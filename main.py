import array
def get_array_as_complex(array):
        return complex(array[0])
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time