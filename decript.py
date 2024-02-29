from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

# Use the same key from the sender side
encryption_key = b'Sixteen_Byte_Key'
cipher = AES.new(encryption_key, AES.MODE_ECB)

# The string representation of bytes
encrypted_message_str =  b"\x15\x05l\xf9\xedw'\t\xd2\x132\x9b: \x0b\x90\xde\xc9\xba\xa1^\xb5\x0b\xac\xd1\x87\xf3\xbe\x9dB\x8e\x95"

# Convert the string representation to actual bytes using eval
# encrypted_message = eval(encrypted_message_str)

decrypted_message = unpad(cipher.decrypt(encrypted_message_str), AES.block_size)

print("Key:", encryption_key)
print("Cipher object:", cipher)
print("Decrypted Message:", decrypted_message.decode('utf-8'))
