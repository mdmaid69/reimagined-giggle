import array
def pop_from_array(array, i=-1):
        return array.pop(i)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time