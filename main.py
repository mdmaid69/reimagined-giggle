def is_palindrome(s):
        return s == s[::-1]
def calculate_energy(mass, c=3*10**8):
        return mass * c**2