import array
def get_array_as_frozenset(array):
        return frozenset(array)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time