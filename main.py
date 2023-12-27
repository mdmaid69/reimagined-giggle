import platform
def get_os_info():
        return platform.uname()
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))