import array
def extend_array(array, iterable):
        array.extend(iterable)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time