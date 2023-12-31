import array
def extend_array(array, iterable):
        array.extend(iterable)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time