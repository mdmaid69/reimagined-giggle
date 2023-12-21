def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import array
def get_array_as_list(array):
        return list(array)