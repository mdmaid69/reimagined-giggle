import array
def insert_into_array(array, i, item):
        array.insert(i, item)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)