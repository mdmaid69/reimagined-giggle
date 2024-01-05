def find_union(list1, list2):
        return set(list1) | set(list2)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)