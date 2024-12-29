import hashlib

# hashlib não está instalado, se for usar esta função: pip install hashlib

def encrypt(password: str):
    '''
    Encrypts the given password using SHA-256 hashing algorithm.

    Args:
      password (str): The password to be encrypted.

    Returns:
      str: The encrypted password.
    '''
    encrypted_password = None

    def encrypt_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    if password is not None and password != "":
        encrypted_password = encrypt_password(password)

    return encrypted_password
