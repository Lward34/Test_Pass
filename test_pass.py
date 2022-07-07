from passlib.hash import sha256_crypt

# input a test password
test_pass="sdev300Key!2"

# Hash the password
hash_pass= sha256_crypt.hash(test_pass)

# view the encrypt password
print("hash_pass")

# Call verify to compare the two entries
print("sha256_crypt.verify(test_pass, hash_pass")