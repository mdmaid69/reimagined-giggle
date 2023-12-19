import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))