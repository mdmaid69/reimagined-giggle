n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)