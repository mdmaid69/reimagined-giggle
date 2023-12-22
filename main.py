import platform
def get_python_version():
        return platform.python_version()
def count_words(sentence):
        return len(sentence.split())