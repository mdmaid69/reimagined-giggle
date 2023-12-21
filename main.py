import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)