import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time