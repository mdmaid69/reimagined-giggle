import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b