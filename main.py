def find_unique_words(sentence):
        return set(sentence.split())
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread