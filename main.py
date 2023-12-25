def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)