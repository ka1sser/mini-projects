# Topic: String methods
# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username mus not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")


if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain any spaces.")
elif not username.isalpha():
    print("Your username can't contain any digits.")
else:
    print(f"Welcome, {username}!")
