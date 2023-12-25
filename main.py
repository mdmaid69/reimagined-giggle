import getpass
def get_username():
        return getpass.getuser()
def count_words(sentence):
        return len(sentence.split())