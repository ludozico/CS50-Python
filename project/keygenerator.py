import os
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
with open('fernet_key.key', 'wb') as key_file:
    key_file.write(key)