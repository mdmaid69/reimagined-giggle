import array
def get_array_as_complex(array):
        return complex(array[0])
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)