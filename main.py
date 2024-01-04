def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import getpass
def get_username():
        return getpass.getuser()