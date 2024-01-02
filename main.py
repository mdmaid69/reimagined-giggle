import array
def get_array_as_frozenset(array):
        return frozenset(array)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time