import array
def get_string_from_array(array):
        return array.tobytes()
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)