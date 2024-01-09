list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))
import shutil
def delete_directory(path):
        shutil.rmtree(path)