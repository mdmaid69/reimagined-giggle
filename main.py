import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time