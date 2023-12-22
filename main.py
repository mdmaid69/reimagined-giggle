import os
def get_environment_variable(var):
        return os.getenv(var)
def count_words(sentence):
        return len(sentence.split())