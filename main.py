import shutil
def move_file(src, dst):
        shutil.move(src, dst)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))