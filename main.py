def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)