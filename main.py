def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}