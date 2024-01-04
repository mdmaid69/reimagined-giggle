import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))