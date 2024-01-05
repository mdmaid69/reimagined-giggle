import getpass
def get_username():
        return getpass.getuser()
def calculate_average(lst):
        return sum(lst) / len(lst)