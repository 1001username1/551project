class UserLogin:
    def __init__(self):
        
        self.users = {
            "username1": "password1",
            "username2": "password2",
            "username3": "password3",
            "username4": "password4",
            "username5": "password5",
        }

    def login(self):
       
        username = input("Please enter the username: ").strip()
        password = input("Enter the password: ").strip()

        if username in self.users:
            if self.users[username] == password:
                print("Login successful! Welcome,", username)
            else:
                print("Password does not match the username.")
        else:
            print("Username not found.")


login_system = UserLogin()
login_system.login()




    
