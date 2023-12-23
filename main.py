import array
def get_array_item_count(array, item):
        return array.count(item)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)