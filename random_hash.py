import hashlib
import random
import string

def generate_random_hash():
    while True:
        # Generate a random string of 32 characters
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        hash_object = hashlib.sha256(random_string.encode())
        hash_hex = hash_object.hexdigest()
        
        # Check if the hash starts with two consecutive zeros
        if hash_hex.startswith('00'):
            print(f"Hash found: {hash_hex}")
            return hash_hex

generate_random_hash()
