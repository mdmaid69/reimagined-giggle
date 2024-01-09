import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])