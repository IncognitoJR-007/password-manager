import json
import os
from encryption_util import encrypt, decrypt
import secrets
import string

class PasswordManager:
    def __init__(self, file_name="passwords.json"):
        self.file_name = file_name
        self.key = b'securepasswordencryptionkey'  # This should be stored securely
    
    def add_password(self, site, username, password):
        encrypted_password = encrypt(password, self.key)
        data = {site: {'username': username, 'password': encrypted_password}}
        
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                stored_data = json.load(file)
        else:
            stored_data = {}
        
        stored_data.update(data)
        
        with open(self.file_name, 'w') as file:
            json.dump(stored_data, file)
    
    def retrieve_password(self, site):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                stored_data = json.load(file)
            
            if site in stored_data:
                username = stored_data[site]['username']
                password = decrypt(stored_data[site]['password'], self.key)
                return {'username': username, 'password': password}
        
        return None

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(characters) for i in range(length))
