def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)