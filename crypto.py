import cryptography
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes



def convert_bytes_to_text(b):
    return b.decode("utf-8")

def convert_text_to_bytes(text):
    return text.encode("utf-8")


def generate_sync_key():
    print("Generating key")
    key = Fernet.generate_key()
    print(key.decode("utf-8")) #We use .decode in order to convert from a bytes option


def get_key_stdin():
    key_text = input().strip()
    key = key_text.encode("utf-8")
    key = Fernet(key)
    return key


def s_encrypt():
    print("Please enter your key")
    key = get_key_stdin()
    print(key)
    text = input("Enter the text to encrypt")
    encrypted = key.encrypt(text.encode("utf-8"))
    print(encrypted.decode("utf-8"))

def s_decrypt():
    print("Please enter your key")
    key = get_key_stdin()
    print("Enter the encrypted text")
    encrypted_text = input().strip()
    encrypted_bytes = encrypted_text.encode("utf-8")

    result = key.decrypt(encrypted_bytes)
    print(result.decode("utf-8"))

   
def conversion_helper(b):
    return base64.b64encode(b).decode("utf-8")

def get_public_key():
    b64String = input()
    data = base64.b64decode(b64String)
    
    key = serialization.load_der_public_key(data)
    return key

def get_private_key():
    b64String = input()
    data = base64.b64decode(b64String)
    
    key = serialization.load_der_private_key(data, password = None)
    return key


def encrypt_async():
    print("Enter public key")
    key = get_public_key()
    print(key)
    text = input("enter text").strip()
    encrypted = key.encrypt(text.encode("utf-8"),padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    print(conversion_helper(encrypted))

def decrypt_async():
    print("Enter private key")

    key = get_private_key()

    print("Enter the encrypted text")
    encrypted_text = input().strip()
    
    encrypted_bytes = base64.b64decode(encrypted_text)
    
    result = key.decrypt(
        encrypted_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    print("\nDecrypted Message:")
    print(result.decode("utf-8"))


def generate_async_key():
    private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            )
    public_key = private_key.public_key()
    private_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption() # Or use BestAvailableEncryption(b'password')
    )
    print("Private Key")
    print(conversion_helper(private_bytes))

    print("\n\nPublic Key")
    public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    print(conversion_helper(public_bytes))

