import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import collections
def create_queue():
        return collections.deque()