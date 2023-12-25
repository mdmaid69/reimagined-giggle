def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array