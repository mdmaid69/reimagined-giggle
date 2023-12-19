import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)