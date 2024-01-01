import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)