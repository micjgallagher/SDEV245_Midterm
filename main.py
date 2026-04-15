import crypto
import cryptography
import hashlib

def read_line_by_file_name(file_name, strip = True):
    """
    Returns first line of file. By default, this will be stripped of any white space.
    """
    file = open(file_name, "r")
    line = file.readline()
    file.close()

    if strip:
        line = line.strip()

    return line

def write_text_to_file(file_name, text):
    """
    This will set the file's contents to the provided string
    """

    file = open(file_name, "w")
    file.write(text)
    file.close()

def user_bool():
    result = input("y/n ")
    return result == "y"


def generate_key():
    print("Generating Fernet key")
    key = cryptography.fernet.Fernet.generate_key()
    key_text = crypto.convert_bytes_to_text(key)
    print(key_text) #Unsure what type key is. This may break

    #Choose to save it
    print("Save this key to file \"key\"")
    if user_bool():
        write_text_to_file("key", key_text)
        print("saved")


def load_key_file():
    text = read_line_by_file_name("key")
    print("Reading Data")
    print(text)
    b = crypto.convert_text_to_bytes(text)
    key = cryptography.fernet.Fernet(b)

    return key


def encrypt():
    print("Load key from file?")
    if user_bool():
        key = load_key_file()
    else:
        print("Please enter your key")
        key = crypto.get_key_stdin()

    print("Enter the text to be encrypted")
    text = input()

    encrypted_text_bytes = key.encrypt(crypto.convert_text_to_bytes(text)) 
    encrypted_text = crypto.convert_bytes_to_text(encrypted_text_bytes)
    print(encrypted_text)
    print("Do you wish to save this data to the file \"data\"")
    if user_bool():
        write_text_to_file("data", encrypted_text)
    #hashing section

    hash = hashlib.sha256()
    hash.update(crypto.convert_text_to_bytes(text))
    hashed= hash.hexdigest()
    print("Hashed message, use this for verification")
    print(hashed)
    print("Save to hash to disk?")
    if user_bool():
        write_text_to_file("hash", hashed)


def main():
    print("Michael Gallagher Module 4 Midterm")

    print("Select an option")
    print("1. Generate Key")
    print("2. Encrypt")
    print("3. Decrypt")


    choice = input()

    if choice == "1":
        generate_key()
    if choice =="2":
        encrypt()




main()
