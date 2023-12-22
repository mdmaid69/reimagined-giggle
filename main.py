def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)