import array
def get_array_as_bytes(array):
        return bytes(array)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)