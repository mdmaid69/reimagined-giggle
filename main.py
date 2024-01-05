import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])