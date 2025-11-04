import hashlib
import os


# text = input("Enter text: ")
# hash_object = hashlib.sha256(text.encode())
# hex_dig = hash_object.hexdigest() #show in hexadecimal
#
# print("SHA is ", hex_dig,)


def hash_file(file_path):
    h = hashlib.new("sha256")
    # open file in binary mode
    # hash by chunks of 1024 bytes
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(1024), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_integrity(file1, file2):
    h1 = hash_file(file1)
    h2 = hash_file(file2)
    print("\nChecking integrity...")

    if h1 == h2:
        return print("Integrity verified.")
    else:
        return print("Integrity not verified. Possible tempering")


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "..", "samples", "test_file.txt")
    file_path2 = os.path.join(current_dir, "..", "samples", "test_file2.txt")
    h = verify_integrity(file_path, file_path2)
    # print(h)
