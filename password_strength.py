import re

def check_password_strength(password):
    length = len(password) >= 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_number = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    strength = 0
    if length: strength += 1
    if has_upper: strength += 1
    if has_lower: strength += 1
    if has_number: strength += 1
    if has_special: strength += 1

    if strength == 5:
        return 'Very Strong'
    elif strength == 4:
        return 'Strong'
    elif strength == 3:
        return 'Moderate'
    else:
        return 'Weak'
