import getpass
def get_username():
        return getpass.getuser()
def calculate_average(numbers):
        return sum(numbers) / len(numbers)