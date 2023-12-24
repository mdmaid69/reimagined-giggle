import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)