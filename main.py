import array
def get_array_slice(array, i, j):
        return array[i:j]
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal