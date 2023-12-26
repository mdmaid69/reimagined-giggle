import array
def insert_into_array(array, i, item):
        array.insert(i, item)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)