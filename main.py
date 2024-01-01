import platform
def get_os_info():
        return platform.uname()
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)