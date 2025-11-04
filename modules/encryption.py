import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# symetric
def aes_ed(message):
    key = secrets.token_bytes(32)
    # init vector random
    nonce = secrets.token_bytes(12)
    aes = AESGCM(key)
    ciphertext = nonce + aes.encrypt(nonce, message.encode(), None)

    # decoding
    # nonce has 12 chars
    plaintext = aes.decrypt(ciphertext[:12], ciphertext[12:], None)
    decoded_message = plaintext.decode()

    return key.hex(), ciphertext.hex(), decoded_message


# asymmetric
def rsa_ed(message):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    #     decrypt with private key + same algorithm
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return ciphertext.hex(), plaintext.decode()


if __name__ == "__main__":
    # r = aes_ed("bububub")
    r = rsa_ed("bububub")
    print(r)
