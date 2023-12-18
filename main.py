list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()