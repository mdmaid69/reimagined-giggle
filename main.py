import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time