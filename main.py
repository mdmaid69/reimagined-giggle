import array
def set_array_item(array, i, item):
        array[i] = item
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)