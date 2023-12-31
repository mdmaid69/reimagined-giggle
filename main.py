import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))