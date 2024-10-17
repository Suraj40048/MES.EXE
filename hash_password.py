import bcrypt

# Example password to hash
password = "admin@123"  # Change this to the password you want to hash

# Hash the password
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Print the hashed password
print(hashed_password.decode('utf-8'))  # This is the value to store in your database
