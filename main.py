import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
n = 10
print("Powers of 2:", [2**x for x in range(n)])