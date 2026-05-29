

from sympy import false


def brute_force_timer(guesses_per_second, password):
    """Estimate the time required to brute-force a password.

    This function computes a very rough time estimate based on the character
    set implied by the password and a given attacker guess rate.
    """
    length = len(password)
    possbilities = 0
    for character in password:
        if character.isupper():
            possbilities += 26
        elif character.islower():
            possbilities += 26
        elif character.isdigit():
            possbilities += 10
        else:
            possbilities += 32

    # Estimate the number of possible combinations for the password.
    total_possbilities = possbilities ** length
    seconds = total_possbilities / guesses_per_second
    if seconds < 1:
        print("Less than 1 second")
        return seconds
    seconds = int(round(seconds))   
    years = seconds // 31_536_000   
    seconds %= 31_536_000

    days = seconds // 86_400
    seconds %= 86_400

    hours = seconds // 3_600
    seconds %= 3_600

    minutes = seconds // 60
    seconds %= 60

    parts = []

    if years > 0:
        parts.append(f"{years} year{'s' if years != 1 else ''}")
    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if seconds > 0:
        parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")
    print("Time to brute-force the password: " + ", ".join(parts))
    return seconds
    

# bruteforce times historically until now:
# password = "P@ssW0rd" #try something easier like "password" or "123456" to see the difference in time to brute-force the password

# print("Password: ", password)

# #1990 
# #Resources: Desktop CPU, early Unix systems
# #Guesses per second: 45
# print("1990:")
# brute_force_timer(45, password)

# #1995
# #Resources: Desktop CPU, early Windows systems
# #Guesses per second: 1000
# print("1995:")
# brute_force_timer(1000, password)

# #2000
# #Resources: PentiumIII, early Athlon CPU and early Windows systems
# #Guesses per second: 100,000
# print("2000:")
# brute_force_timer(100_000, password)

# #2005
# #Resources: Dual-core CPUs, early multi-core systems
# #Guesses per second: 1,000,000
# print("2005:")
# brute_force_timer(1_000_000, password)

# #2010
# #Resources: Quad-core CPUs, early GPUs for password cracking
# #Guesses per second: 100,000,000
# print("2010:")
# brute_force_timer(100_000_000, password)

# #2015
# #Resources: High-end CPUs, advanced GPUs, and distributed computing
# #Guesses per second: 10,000,000,000
# print("2015:")
# brute_force_timer(10_000_000_000, password)

# #2020
# #Resources: High-end CPUs, RTX 3090 GPUs, and distributed computing
# #Guesses per second: 60,000,000,000
# print("2020:")
# brute_force_timer(60_000_000_000, password)

# #2025
# #Resources: High-end CPUs, RTX 4090 GPUs, and distributed computing
# #Guesses per second: 250,000,000,000
# print("2025:")
# brute_force_timer(250_000_000_000, password)