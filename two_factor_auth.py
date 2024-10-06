import random

def send_2fa_code(email):
    # Simulating sending a 2FA code (normally done via email/SMS)
    code = random.randint(100000, 999999)
    print(f"Sending 2FA code {code} to {email}")
    return code

def verify_2fa_code(sent_code, user_code):
    return str(sent_code) == str(user_code)
