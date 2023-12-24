import platform
def get_os_info():
        return platform.uname()
def calculate_average(lst):
        return sum(lst) / len(lst)