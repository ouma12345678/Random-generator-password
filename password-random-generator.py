import random
import string

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage:
random_password = generate_password()
print("Randomly generated password:", random_password) 


