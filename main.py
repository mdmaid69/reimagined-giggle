import array
def check_if_array_contains_item(array, item):
        return item in array
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)