import getpass
def get_username():
        return getpass.getuser()
def remove_duplicates(lst):
        return list(set(lst))