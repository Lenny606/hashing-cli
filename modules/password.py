from zxcvbn import zxcvbn
from getpass import getpass
import bcrypt

def check_pass_strength(password_input):
    password_input = zxcvbn(password_input)
    score = password_input["score"]

    if score < 3:

        feedback = password_input.get("feedback")
        warning = feedback.get("warning")
        suggestions = feedback.get("suggestions")
        response = "Password is weak. Try to increase it."
        response += "Warning: " + warning + "\nSuggestions: "
        for suggestion in suggestions:
            response += suggestion + "\n"

    elif score < 4:
        response = "Password is good."
    else:
        response = "Password is strong."
    return response,score

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def verify_password(password, hashed) -> bool:
    return bcrypt.checkpw(password.encode(), hashed)

if __name__ == "__main__":
    while True:
        password = getpass("Enter password: ")
        r = check_pass_strength(password)
        print(r[0])

        if r[1] >= 4:
            break
        else:
            print("Try again.")

    hashed = hash_password(password)
    print("Hashed password: ", hashed)
    print("Verifying password...")
    if verify_password(password, hashed):
        print("Password verified.")