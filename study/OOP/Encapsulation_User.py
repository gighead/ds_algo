class User:
    def __init__(self, userName=None, password=None):
        self.__userName = userName
        self.__password = password

    def login(self, userName, password):
        if ((self.__userName.lower() == userName.lower())
                and (self.__password == password)):
            print(
                "Access Granted against username:",
                self.__userName.lower(),
                "and password:",
                self.__password)
        else:
            print("Invalid Credentials!")

    def displayUser(self):
        return (self.__userName)

    def changePassword(self, password=None):
        self.__password = password


# created a new User object and stored the password and username
Steve = User("Steve", "12345")
Steve.login("steve", "12345")  # Grants access because credentials are valid
# does not grant access since the credentails are invalid
Steve.login("steve", "6789")
print(Steve.displayUser())
Steve.changePassword('newpass')
Steve.login("steve", "12345")
Steve.login("steve", "newpass")