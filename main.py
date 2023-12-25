import array
def convert_array_to_bytes(array):
        return array.tobytes()
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal