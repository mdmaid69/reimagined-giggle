import array
def get_array_index(array, item):
        return array.index(item)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time