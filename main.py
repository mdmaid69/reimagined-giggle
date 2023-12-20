import array
def get_array_as_int(array):
        return int(array[0])
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)