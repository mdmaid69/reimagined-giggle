import getpass
def get_username():
        return getpass.getuser()
def find_difference(list1, list2):
        return set(list1) - set(list2)