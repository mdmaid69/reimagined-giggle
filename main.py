import array
def get_array_as_frozenset(array):
        return frozenset(array)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal