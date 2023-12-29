import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))