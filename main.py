import platform
def get_os_info():
        return platform.uname()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())