import math




def asses_password_strength(password):
    score = 0
    length = len(password)
    if length == 0:
        print("Password cannot be empty.")
        return
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    if length >= 20:
        score += 5
    if length < 8:
        print("Password is too short, it should be at least 8 characters long.")

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

    if (length == upperCharacters) or (length == lowerCharacters) or (length == digits) or (length == specialCharacters):
        if length == upperCharacters:
            print("Password should not consist of only uppercase letters.")
        elif length == lowerCharacters:
            print("Password should not consist of only lowercase letters.")
        elif length == digits:
            print("Password should not consist of only digits.")
        elif length == specialCharacters:
            print("Password should not consist of only special characters.")
        score -= 5

    common_passwords = open("common_passwords", "r").read().splitlines()

    if password.lower() in common_passwords:
        print("Password is too common, please choose a stronger password." + " It is recommended to use a password that is not found in common password lists.")    
        score = -10
        print("score: ", score)
        return score

    R = 0
    if upperCharacters > 0:
        R += 26
    if lowerCharacters > 0:
        R += 26
    if digits > 0:
        R += 10
    if specialCharacters > 0:
        R += 32

    entropy = length * (math.log2(R))

    if entropy < 30:
        score -= 5 
        print("Password is very weak. Entropy: ", entropy)
    elif entropy < 50:
        score -= 5
        print("Password is weak. Entropy: ", entropy)
    elif entropy < 70:
        score += 1
        print("Password is moderate. Entropy: ", entropy)
    elif entropy < 100:
        score += 5
        print("Password is strong. Entropy: ", entropy)
    else:
        score += 10
        print("Password is very strong. Entropy: ", entropy)

    if score < 0:
        print("Your password is  very weak, consider changing it ASAP. Score: ", score)
    elif score == 0:
        print("Your password is weak, consider improving it. Score: ", score)
    elif score < 5:
        print("Your password is moderate, consider improving it. Score: ", score)
    elif score < 10:
        print("Your password is strong, but it could be stronger. Score: ", score)
    else:
        print("Your password is very strong. Score: ", score)
    return score


test_passwrods= ["password", "Password", "Password123", "P@ssw0rd!", "P@ssw0rd!2024", "P@ssw0rd!2024$%^&*()_+"]
scores = [] 
for i in range(len(test_passwrods)):
    scores.append(asses_password_strength(test_passwrods[i])) 

print("Test passwords and their scores:")
for i in range(len(test_passwrods)):
    print(f"{test_passwrods[i]}: {scores[i]}")  


