import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
def greet(name):
        print(f"Hello, {name}!")