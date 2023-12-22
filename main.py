import array
def get_array_slice(array, i, j):
        return array[i:j]
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)