import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
def find_union(list1, list2):
        return set(list1) | set(list2)