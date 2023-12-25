import array
def convert_array_to_string(array):
        return array.tostring()
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)