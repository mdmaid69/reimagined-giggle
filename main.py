import array
def remove_from_array(array, item):
        array.remove(item)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)