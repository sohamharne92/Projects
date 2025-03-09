import secrets
import string

def secure_shuffle(password_list):
    for i in range(len(password_list) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_list[i], password_list[j] = password_list[j], password_list[i]

def generate_password(length):
    if length < 8 or length > 15:
        print("Password length should be between 8 and 15 characters for security.")
        return None

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    password = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    all_characters = lower + upper + digits + special
    password += [secrets.choice(all_characters) for _ in range(length - 4)]

    secure_shuffle(password)

    return ''.join(password)

try:
    length = int(input("Enter the desired password length (8 to 15): "))
    password = generate_password(length)
    if password:
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
