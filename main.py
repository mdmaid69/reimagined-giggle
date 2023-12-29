import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def is_palindrome(s):
        return s == s[::-1]