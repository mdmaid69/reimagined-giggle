def count_characters(sentence):
        return len(sentence)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread