import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
def count_words(sentence):
        return len(sentence.split())