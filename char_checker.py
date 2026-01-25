print("******\n Welcome to internet \n * Please Choose Your Username * \n * Please enter your password *\n******")

username=str(input("Enter your username: "))
password=str(input("Enter your password: "))

for char in username:
    if len(username) < 6:
        print("Error: Username must be at least 6 characters long.")
        break
    elif char in username == "!@#$%^&*()":
        print("Error: Username cannot contain special characters.")
        break
    else:
        continue


for char in password:
    if char in username:
        print("Error: Password cannot contain any part of the username.")
        break
    elif len(password) < 6:
        print("Error: Password must be at least 6 characters long.")
        break
    elif char in password == " ":
        print("Error: Password cannot contain spaces.")
        break
    elif char in password == "!@#$%^&*()":
        print("Error: Password cannot contain special characters.")
        break