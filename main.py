import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time