import array
def get_bytes_from_array(array):
        return array.tobytes()
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time