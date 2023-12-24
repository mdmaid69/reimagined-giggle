import array
def convert_array_to_unicode(array):
        return array.tounicode()
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)