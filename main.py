import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
n = 10
print("Square numbers:", [x**2 for x in range(n)])