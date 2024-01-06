import platform
def get_os_info():
        return platform.uname()
def calculate_pressure(force, area):
        return force / area