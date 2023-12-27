import platform
def get_os_info():
        return platform.uname()
def calculate_volume(length, width, height):
        return length * width * height