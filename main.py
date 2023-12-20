import array
def set_array_item(array, i, item):
        array[i] = item
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)