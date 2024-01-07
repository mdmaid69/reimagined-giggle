import platform
def get_os_info():
        return platform.uname()
def calculate_average(numbers):
        return sum(numbers) / len(numbers)