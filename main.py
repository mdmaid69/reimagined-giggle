import array
def get_array_item_count(array, item):
        return array.count(item)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal