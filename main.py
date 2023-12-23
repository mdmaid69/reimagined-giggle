list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)