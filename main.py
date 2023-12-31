def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import array
def reverse_array(array):
        array.reverse()