import array
def get_list_from_array(array):
        return array.tolist()
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time