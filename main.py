import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())