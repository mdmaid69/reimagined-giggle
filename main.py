import array
def get_array_as_list(array):
        return list(array)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time