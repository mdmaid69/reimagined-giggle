import array
def get_array_slice(array, i, j):
        return array[i:j]
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)