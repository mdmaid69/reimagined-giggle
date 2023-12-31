import array
def get_array_item_count(array, item):
        return array.count(item)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)