import getpass
def get_username():
        return getpass.getuser()
def find_unique_words(sentence):
        return set(sentence.split())