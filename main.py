def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import array
def pop_from_array(array, i=-1):
        return array.pop(i)