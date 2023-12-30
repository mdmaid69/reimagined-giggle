import array
def convert_array_to_bytes(array):
        return array.tobytes()
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)