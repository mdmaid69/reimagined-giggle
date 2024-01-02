def count_words(sentence):
        return len(sentence.split())
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread