class User:
    def __init__(self, username, password):
        # Initialize username and password
        self.username = username
        self.__password = password  # Fixed initialization

    def log_in(self, password):
        # Check the password and log the user in
        if self.__check_password(password):
            print(f'Welcome, {self.username}!')
        else:
            print('Incorrect password')

    def __check_password(self, password):
        # Compare the given password with the stored password
        return password == self.__password


# Create a User instance
user = User('john_doe', 'securepassword123')

# Test log_in with different passwords
user.log_in('securepassword123')  # Correct password
user.log_in('wrongpassword')      # Incorrect password

# Accessing private method (not recommended)
print(user._User__check_password('securepassword123'))  # True        
        
