import platform
def get_python_version():
        return platform.python_version()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())