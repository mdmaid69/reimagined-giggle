def calculate_volume(length, width, height):
        return length * width * height
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True