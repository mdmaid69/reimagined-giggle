def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import array
def check_if_array_contains_item(array, item):
        return item in array