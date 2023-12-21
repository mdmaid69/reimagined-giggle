import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)