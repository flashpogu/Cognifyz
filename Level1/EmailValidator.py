"""Develop a Python function that validates
whether a given string is a valid email
address. Implement checks for the format,
including the presence of an "@" symbol and
a domain name"""

def is_valid_email(email):
    if "@" not in email or email.count("@") != 1:
        return False
    local, domain = email.split("@")
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    if ".." in domain:
        return False
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-")
    if not set(local).issubset(allowed):
        return False
    return True


print(is_valid_email("rr@rrr.com"))
print(is_valid_email("abcde"))