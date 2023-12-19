import array
def check_if_array_contains_item(array, item):
        return item in array
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))