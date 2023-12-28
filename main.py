import glob
def find_files(pattern):
        return glob.glob(pattern)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))