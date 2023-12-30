import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)