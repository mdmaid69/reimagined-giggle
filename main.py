import time
def get_current_time():
        return time.ctime()
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))