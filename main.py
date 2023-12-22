import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal