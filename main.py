import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())