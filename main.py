import array
def get_bytes_from_array(array):
        return array.tobytes()
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)