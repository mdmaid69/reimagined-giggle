import datetime
def get_current_date():
        return datetime.date.today()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"