import array
def clear_array(array):
        array *= 0
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)