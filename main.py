import os
def get_environment_variable(var):
        return os.getenv(var)
def find_unique_words(sentence):
        return set(sentence.split())