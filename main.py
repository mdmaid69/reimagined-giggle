list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))
import shutil
def move_file(src, dst):
        shutil.move(src, dst)