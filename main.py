import array
def get_array_as_repr(array):
        return repr(array)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)