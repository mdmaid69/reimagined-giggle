import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time