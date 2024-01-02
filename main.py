import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
i = 0
while i < 5:
        print(i)
        i += 1