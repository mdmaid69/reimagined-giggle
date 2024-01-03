import array
def iterate_over_array(array):
        for item in array:
        print(item)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))