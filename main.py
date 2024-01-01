import array
def get_array_itemsize(array):
        return array.itemsize
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)