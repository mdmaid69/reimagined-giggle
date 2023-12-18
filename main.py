def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import array
def extend_array(array, iterable):
        array.extend(iterable)