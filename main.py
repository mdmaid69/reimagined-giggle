import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])