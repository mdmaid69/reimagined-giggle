import array
def get_list_from_array(array):
        return array.tolist()
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time