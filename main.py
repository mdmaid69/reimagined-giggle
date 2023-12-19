import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)