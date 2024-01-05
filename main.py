def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import array
def pop_from_array(array, i=-1):
        return array.pop(i)