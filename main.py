import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time