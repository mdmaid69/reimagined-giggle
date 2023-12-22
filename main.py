import sys
def add_to_python_path(path):
        sys.path.append(path)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))