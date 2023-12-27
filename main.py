import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
def calculate_volume(length, width, height):
        return length * width * height