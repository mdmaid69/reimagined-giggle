n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array