import platform
def get_os_info():
        return platform.uname()
def find_unique_words(sentence):
        return set(sentence.split())