import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time