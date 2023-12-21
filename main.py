import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
def find_unique_words(sentence):
        return set(sentence.split())