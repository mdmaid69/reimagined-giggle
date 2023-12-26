import platform
def get_python_version():
        return platform.python_version()
def calculate_roi(gain, cost):
        return (gain - cost) / cost