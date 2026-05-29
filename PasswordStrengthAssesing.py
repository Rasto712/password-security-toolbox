import math


def asses_password_strength(password):
    """Score a password based on length, variety, and entropy."""
    length = len(password)

    if length == 0:
        print("Password cannot be empty.")
        return 0

    upperCharacters = 0
    lowerCharacters = 0
    digits = 0
    specialCharacters = 0

    for character in password:
        if character.isupper():
            upperCharacters += 1
        elif character.islower():
            lowerCharacters += 1
        elif character.isdigit():
            digits += 1
        else:
            specialCharacters += 1

    # Load a list of common passwords to penalize very easy guesses.
    try:
        common_passwords = open("common_passwords", "r").read().splitlines()
        common_passwords = [item.lower() for item in common_passwords]
    except FileNotFoundError:
        common_passwords = []

    if password.lower() in common_passwords:
        print("Password is too common. Please choose a stronger password.")
        print("Score: 0/20")
        return 0

    R = 0

    # Determine the set size implied by the characters used in the password.
    if upperCharacters > 0:
        R += 26
    if lowerCharacters > 0:
        R += 26
    if digits > 0:
        R += 10
    if specialCharacters > 0:
        R += 32

    entropy = length * math.log2(R)

    score = 0

    # Entropy score: max 12 points
    if entropy >= 100:
        score += 12
    elif entropy >= 80:
        score += 10
    elif entropy >= 70:
        score += 8
    elif entropy >= 60:
        score += 6
    elif entropy >= 40:
        score += 4
    elif entropy >= 30:
        score += 2
    else:
        score += 0

    # Length score: max 4 points
    if length >= 20:
        score += 4
    elif length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        score -= 4

    # Character variety score: max 4 points
    if lowerCharacters > 0:
        score += 1
    if upperCharacters > 0:
        score += 1
    if digits > 0:
        score += 1
    if specialCharacters > 0:
        score += 1

    # Penalties
    if length < 8:
        print("Password is too short. It should be at least 8 characters long.")

    if length == upperCharacters:
        print("Password should not consist of only uppercase letters.")
        score -= 5
    elif length == lowerCharacters:
        print("Password should not consist of only lowercase letters.")
        score -= 5
    elif length == digits:
        print("Password should not consist of only digits.")
        score -= 5
    elif length == specialCharacters:
        print("Password should not consist of only special characters.")
        score -= 5

    if len(set(password)) == 1:
        print("Password should not be made of one repeated character.")
        score -= 5

    # Keep score between 0 and 20
    if score < 0:
        score = 0
    elif score > 20:
        score = 20

    if score < 4:
        strength = "Very Weak"
    elif score < 8:
        strength = "Weak"
    elif score < 12:
        strength = "Moderate"
    elif score < 16:
        strength = "Strong"
    else:
        strength = "Very Strong"

    print(f"Password is {strength}. Entropy: {round(entropy, 2)}")
    print(f"Score: {score}/20")

    return score

# test_passwrods= ["password", "Password", "Password123", "P@ssw0rd!", "P@ssw0rd!2024", "P@ssw0rd!2024$%^&*()_+"]
# scores = [] 
# for i in range(len(test_passwrods)):
#     scores.append(asses_password_strength(test_passwrods[i])) 

# print("Test passwords and their scores:")
# for i in range(len(test_passwrods)):
#     print(f"{test_passwrods[i]}: {scores[i]}")  


