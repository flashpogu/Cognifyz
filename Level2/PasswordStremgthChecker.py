"""Create a Python function that evaluates
the strength of a password entered by the
user. Implement checks for factors such as
length, presence of uppercase and
lowercase letters, digits, and special
characters."""

def password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = set("!@#$%^&*(),.?\":{}|<>")
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    
    if not has_upper:
        return "Weak: Password must contain at least one uppercase letter."
    if not has_lower:
        return "Weak: Password must contain at least one lowercase letter."
    if not has_digit:
        return "Weak: Password must contain at least one digit."
    if not has_special:
        return "Weak: Password must contain at least one special character."
    
    return "Strong: Password meets all criteria."

print(password_strength("Password123!"))