import array
def append_to_array(array, item):
        array.append(item)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)