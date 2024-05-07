import os
import ast
class User:
    def __init__(self):
        self.database = {}

    def register(self):

        while True:
            try:
                username = input("Enter username:")
                while len(username) < 4:
                    print("Username must be greater than eigth (8)")
                    username = input("Enter username:")

                password = input("Enter your password: ")
                while len(password) < 8:
                    print("Password must be greater than eith (8) charcaters")
                    password = input("Enter your password: ")

                verify_pass = input("Enter your password: ")
                while password != verify_pass:
                    print("Passwords do not match. Please try again.")
                    verify_pass = input("Enter your password: ")
                
                user_info = {'Name': username, 'Password': password, 'Score': 0}

                with open("Users.txt", 'w') as file:
                    file.write(str(user_info, '\n'))

            except ValueError as e:
                print(f"Error {e}")

    def login(self):
        while True:
            
            # To build logic if User.txt Exist
            try:
                username = input ("Enter username: ")
                with open('User.txt', 'r') as file:
                    for line in file:
                        user_info = ast.literal_eval(line.strip())
                        if user_info['Name'] == username:
                            print("User found.")
                        
                        password = input("Enter password: ")
                        if user_info['Password'] == password:
                            print('Log in successful.')
            except ValueError as e:
                print(f"Error {e}")