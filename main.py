import array
def convert_array_to_list(array):
        return array.tolist()
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time