import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])