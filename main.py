import array
def extend_array(array, iterable):
        array.extend(iterable)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal