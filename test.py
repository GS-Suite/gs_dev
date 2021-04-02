import argon2, binascii

hash = argon2.hash_password_raw(
    time_cost=16, memory_cost=2**15, parallelism=2, hash_len=32,
    password=b'password', salt=b'some salt', type=argon2.low_level.Type.ID)
print("Argon2 raw hash:", binascii.hexlify(hash))

# argon2Hasher = argon2.PasswordHasher(
#     time_cost=16, memory_cost=2**15, parallelism=2, hash_len=32, salt_len=16)
# hash = argon2Hasher.hash("password")
# print("Argon2 hash (random salt):", hash)

verifyValid = argon2.verify_password(
    hash,
    "password",
    argon2.low_level.Type.ID )
print("Argon2 verify (correct password):", verifyValid)