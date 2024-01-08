def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)