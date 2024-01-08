import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time