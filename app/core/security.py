import bcrypt


# To hash password
def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")[:72]

    hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_bytes.decode("utf-8")

# To compare login password hash against saved password hash
def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_bytes = plain_password.encode("utf-8")[:72]
    hashed_bytes = hashed_password.encode("utf-8")
    
    return bcrypt.checkpw(password_bytes, hashed_bytes)