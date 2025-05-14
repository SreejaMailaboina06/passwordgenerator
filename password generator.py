import random
import string

def generate_unique_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    # Define character pools
    char_sets = []
    if use_upper:
        char_sets.append(list(string.ascii_uppercase))
    if use_lower:
        char_sets.append(list(string.ascii_lowercase))
    if use_digits:
        char_sets.append(list(string.digits))
    if use_special:
        char_sets.append(list("!@#$%^&*()-_=+[]{};:,.<>?/"))

    if not char_sets:
        return "Error: No character types selected."

    # Combine all selected characters and remove duplicates
    all_chars = list(set(char for subset in char_sets for char in subset))

    # Ensure password is not longer than unique character set
    if length > len(all_chars):
        return "Error: Requested length exceeds unique character pool size."

    # Ensure password contains at least one character from each selected category
    password = [random.choice(subset) for subset in char_sets]

    # Fill remaining characters without duplicates
    remaining_chars = list(set(all_chars) - set(password))
    random.shuffle(remaining_chars)
    password += remaining_chars[:length - len(password)]

    # Shuffle final password for randomness
    random.shuffle(password)
    return ''.join(password)

# Example usage
print(generate_unique_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True))


