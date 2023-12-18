def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import os
def get_environment_variable(var):
        return os.getenv(var)