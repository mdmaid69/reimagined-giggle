import array
def get_array_item_count(array, item):
        return array.count(item)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)