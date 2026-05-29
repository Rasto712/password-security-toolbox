import hashlib
import secrets
import hmac


def hash_password(password, pepper="", iterations=600_000):
    """Hash a password using PBKDF2 with SHA-256, salt, and optional pepper."""
    # Generate a cryptographically secure random salt for this password.
    salt = secrets.token_hex(16)

    combined_password = password + pepper

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        combined_password.encode(),
        salt.encode(),
        iterations
    ).hex()

    # Return the hash details needed for password verification later.
    return {
        "hash": password_hash,
        "salt": salt,
        "iterations": iterations
    }

    