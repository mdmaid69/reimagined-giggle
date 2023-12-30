import array
def get_array_index(array, item):
        return array.index(item)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal