import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])