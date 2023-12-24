def calculate_roi(gain, cost):
        return (gain - cost) / cost
import platform
def get_os_info():
        return platform.uname()