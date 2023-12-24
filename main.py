import array
def insert_into_array(array, i, item):
        array.insert(i, item)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time