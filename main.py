def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)