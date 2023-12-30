import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])