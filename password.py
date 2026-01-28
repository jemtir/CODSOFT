import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    while True:
        pwd = ""
        has_number = False
        has_special = False

        for _ in range(min_length):
            new_char = random.choice(characters)
            pwd += new_char

            if new_char in digits:
                has_number = True
            elif new_char in special:
                has_special = True

        if (not numbers or has_number) and (not special_characters or has_special):
            return pwd


# -------- Main Program --------
min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want numbers? (y/n): ").lower() == "y"
has_special = input("Do you want special characters? (y/n): ").lower() == "y"

password = generate_password(min_length, has_number, has_special)
print("\nGenerated Password:", password)
