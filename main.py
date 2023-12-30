import array
def iterate_over_array(array):
        for item in array:
        print(item)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)