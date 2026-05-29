# Password Security Toolbox

Created by **Rastislav Mintal**
Date: **28.05.2026**

A simple cybersecurity toolbox focused on good password practices.
This project includes tools for password strength assessment, brute-force time estimation, and password hashing demonstrations.

> **Educational purpose only:** This project is designed to help users understand password security concepts. Do not use it to collect, store, or test other people's passwords.

---

## BruteForceTimer.py

Calculates how long it would take for a brute-force algorithm to guess a user's password in a worst-case scenario.

This file also includes a historical overview showing how password cracking speeds have improved over time.

Users can test different passwords and compare how long they might take to brute force using different hardware-era estimates.

Example passwords to analyze:

```text
password
p@ssw0rd
P@ssW0rD123
000000
123456
```

You can also test your own password.

**Important note:**
The brute-force estimate is theoretical. Real attackers often use dictionary attacks, leaked password lists, pattern matching, and rule-based attacks before trying pure brute force.

---

## PassWordHasher.py

Demonstrates password hashing using a salt, optional pepper, and multiple iterations.

The function returns:

```text
hashed value
salt
number of iterations
```

This file is meant to show what safer password storage practices can look like.

If you use this concept in your own application, keep these rules in mind:

* Never store the original password.
* Store only the hashed password, the salt, and the number of iterations.
* The salt must be saved. Without the salt, the password cannot be verified.
* Peppers should not be stored directly in the code.
* Peppers should be stored separately, such as in an environment variable or secure configuration.
* When verifying a password, load the pepper from a separate secure location.
* Do not use broken or outdated hash functions like SHA-1.
* For real password storage, prefer proven password-hashing algorithms such as PBKDF2, bcrypt, scrypt, or Argon2.

---

## PasswordGenerator.py

Generates a random password using uppercase letters, lowercase letters, digits, and punctuation. If the requested length is shorter than 8 characters, the generator automatically uses a safer minimum length.

This file can be used to create strong example passwords, and it also includes optional hooks to assess the generated password strength and brute-force resistance.

---

## PersonalPasswordRiskAnalyzer.py

Analyzes a password for exposure of personal information. It checks whether the password contains values such as a name, email username, phone number digits, birth date parts, or address components.

The analyzer returns a risk score, a risk level (Low/Moderate/High), and warnings to help identify why a password may be more vulnerable because of personal data.

---

## PasswordStrengthAssessing.py

Scores the strength of a password.

The higher the score, the stronger the password is considered to be.

The function checks:

* Password length
* Character variety
* Common password usage
* Password entropy
* Simple weak patterns

Users can test their own password and see how it scores.

### Score Assessment

```text
score < 0:
    Very weak password. You should change it as soon as possible.

score == 0:
    Weak password. Consider changing or improving it.

score < 5:
    Moderate password. Consider improving it.

score <= 10:
    Strong password, but it could be stronger.

score > 10:
    Very strong password.
```

---

## Good Password Practices

A good password should:

* Be at least 12–16 characters long
* Use uppercase and lowercase letters
* Include numbers
* Include special characters
* Avoid common words
* Avoid repeated characters like `000000`
* Avoid predictable patterns like `Password123!`
* Avoid personal information such as names, birthdays, or usernames

A stronger password example:

```text
Blue-Summer-2026!River#91
```

---

## Disclaimer

This project provides educational estimates and demonstrations.
Password security depends on many factors, including hashing algorithms, hardware, password reuse, leaked databases, and attack methods.
