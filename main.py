def is_palindrome(s):
        return s == s[::-1]
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()