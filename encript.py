from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Replace 'my_custom_key' with your own 16-byte key
custom_key = b'Sixteen_Byte_Key'
cipher = AES.new(custom_key, AES.MODE_ECB)

# Your original code to encrypt a message
message = "Hello, world!"
encrypted_message = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))

print("Key:", custom_key)
print("Cipher object:", cipher)
print("Encrypted Message:", encrypted_message)
