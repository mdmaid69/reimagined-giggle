import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import itertools
print(list(itertools.permutations([1, 2, 3])))