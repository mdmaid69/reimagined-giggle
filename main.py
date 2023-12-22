import array
def get_array_typecode(array):
        return array.typecode
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)