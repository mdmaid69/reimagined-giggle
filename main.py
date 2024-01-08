import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)