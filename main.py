import array
def get_array_as_bytearray(array):
        return bytearray(array)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal