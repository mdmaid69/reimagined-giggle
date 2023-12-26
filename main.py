def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}