import array
def get_array_index(array, item):
        return array.index(item)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)