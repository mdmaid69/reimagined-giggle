def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import platform
def get_os_info():
        return platform.uname()