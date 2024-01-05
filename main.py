import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
def find_union(list1, list2):
        return set(list1) | set(list2)