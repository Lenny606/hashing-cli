from modules.hash import hash_file, verify_integrity
from modules.password import hash_password, verify_password, check_pass_strength
from modules.encryption import aes_ed, rsa_ed


def menu():
    print("1. Hash file")
    print("2. Verify file integrity")
    print("3. Hash password")
    print("4. Verify password")
    print("5. Check password strength")
    print("6. Encrypt")
    print("7. Decrypt")
    print("8. Exit")
    choice = input("Enter your choice: ")


print("Welcome to hashing-cli!")

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "8":
        break
    elif choice == "1":
        file_path = input("Enter file path: ")
        print("Hashed file: ", hash_file(file_path))
    elif choice == "2":
        file_path = input("Enter file path: ")
        file_path2 = input("Enter file path: ")
        print("Integrity verified: ", verify_integrity(file_path, file_path2))
    elif choice == "3":
        password = input("Enter password: ")
        hashed = hash_password(password)
        print("Hashed password: ", hashed)
    elif choice == "4":
        password = input("Enter password: ")
        hashed = hash_password(password)
        print("Verifying password...")
        if verify_password(password, hashed):
            print("Password verified.")
        else:
            print("Password not verified.")
    elif choice == "5":
        password = input("Enter password: ")
        r = check_pass_strength(password)
        print(r[0])
    elif choice == "6":
        text = input("Enter text: ")
        print("Encrypted text: ", aes_ed(text))
    elif choice == "7":
        text = input("Enter text: ")
        print("Decrypted text: ", aes_ed(text))
print("Exiting...")
