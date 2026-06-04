class PasswordException(Exception):
    pass


class LoginException(Exception):
    pass


class SignUp:

    def __init__(self, fn, ln, un, pwd):
        self.fn = fn
        self.ln = ln
        self.un = un
        self.pwd = pwd


class SignIn:

    def __init__(self, un, pwd):
        self.un = un
        self.pwd = pwd

    def loginCheck(self, signup):

        if signup.un == self.un and signup.pwd == self.pwd:
            print(f"Welcome {signup.fn} {signup.ln}")

        else:
            raise LoginException("Invalid Username or Password")


while True:

    try:

        fn = input("Enter First Name: ")
        ln = input("Enter Last Name: ")
        un = input("Enter Username: ")
        pwd = input("Enter Password: ")

        if len(pwd) < 8:
            raise PasswordException(
                "Password must contain minimum 8 characters"
            )

        if len(pwd) > 16:
            raise PasswordException(
                "Password must contain maximum 16 characters"
            )

        if not any(ch.islower() for ch in pwd):
            raise PasswordException(
                "Password must contain at least one lowercase letter"
            )

        if not any(ch.isupper() for ch in pwd):
            raise PasswordException(
                "Password must contain at least one uppercase letter"
            )

        if not any(ch.isdigit() for ch in pwd):
            raise PasswordException(
                "Password must contain at least one digit"
            )

        if not any(not ch.isalnum() for ch in pwd):
            raise PasswordException(
                "Password must contain at least one special character"
            )

        signup = SignUp(fn, ln, un, pwd)
        break

    except PasswordException as e:
        print(e)
        print("Try Again\n")


signin = SignIn(
    input("Enter Username: "),
    input("Enter Password: ")
)

try:
    signin.loginCheck(signup)

except LoginException as e:
    print(e)