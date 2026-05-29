import random
import string


def generate_password(length):
    """Generate a random password with letters, digits, and symbols."""
    if length < 8:
        print("Password should be at least 8 characters long for better security. Setting length to 8.")
        length = 8

    # Use a broad character set to increase password variety.
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

new_password = generate_password(20)
print("Generated password: ", new_password)

#optional to test
import PasswordStrengthAssesing
import BruteForceTimer
print("Assessing password strength...")
PasswordStrengthAssesing.asses_password_strength(new_password)
print("Calculating time to brute-force the password...")
BruteForceTimer.brute_force_timer(1_000_000_000, new_password)