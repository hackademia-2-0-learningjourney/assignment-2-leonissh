import json
import os

user_data_file = 'user_data.json'
def sign_up():
    username = input("Enter a Username: ")
    password = input("Enter a Password: ")
    mobile_number = input("Enter your Mobile Number: ")

    new_user = {
        "username": username,
        "password": password,
        "mobile_number": mobile_number
    }

    if os.path.exists(user_data_file):
        with open(user_data_file, 'r') as file:
            user_data = json.load(file)
    else:
        user_data = []

    user_data.append(new_user)

    with open(user_data_file, 'w') as file:
        json.dump(user_data, file, indent=4)

    print("Sign-Up successful!")

def sign_in():
    username = input("Enter your Username: ")
    password = input("Enter your Password: ")

    if os.path.exists(user_data_file):
        with open(user_data_file, 'r') as file:
            user_data = json.load(file)
    else:
        print("No users have signed up yet.")
        return

    for user in user_data:
        if user['username'] == username and user['password'] == password:
            print(f"Welcome to the device, {username}!")
            print(f"Your mobile number is: {user['mobile_number']}")
            return

    print("Incorrect credentials. Program terminated.")

def main():
    print("1. Sign Up")
    print("2. Sign In")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        sign_up()
    elif choice == '2':
        sign_in()
    else:
        print("Invalid choice. Program terminated.")

if __name__ == "__main__":
    main()
