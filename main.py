import array
def get_array_item_count(array, item):
        return array.count(item)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])