import array
def set_array_item(array, i, item):
        array[i] = item
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time