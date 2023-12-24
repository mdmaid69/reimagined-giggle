import array
def get_array_as_frozenset(array):
        return frozenset(array)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)