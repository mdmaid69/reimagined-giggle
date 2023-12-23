import array
def get_array_item_count(array, item):
        return array.count(item)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time