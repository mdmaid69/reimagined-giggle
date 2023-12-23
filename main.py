def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)