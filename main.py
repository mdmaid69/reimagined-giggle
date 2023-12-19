import platform
def get_python_version():
        return platform.python_version()
def find_unique_words(sentence):
        return set(sentence.split())