import array
def get_array_as_float(array):
        return float(array[0])
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)