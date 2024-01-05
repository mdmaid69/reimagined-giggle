import collections
def create_user_dict():
        return collections.UserDict()
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())