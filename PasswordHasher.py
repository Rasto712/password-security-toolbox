import hashlib
import secrets
import hmac


def hash_password(password, pepper="", iterations=600_000):
    salt = secrets.token_hex(16)

    combined_password = password + pepper

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        combined_password.encode(),
        salt.encode(),
        iterations
    ).hex()

    return {
        "hash": password_hash,
        "salt": salt,
        "iterations": iterations
    }

    