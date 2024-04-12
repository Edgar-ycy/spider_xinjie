import base64
from base64 import b64encode,b64decode
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from Cryptodome.Random import get_random_bytes

sensitive_data = b"YCY125698dffffffffffffffffffffffffffffffffffffffffffffff"
# key = get_random_bytes(16) #must be 16, 24 or 32 bytes long      秘钥
key = b64decode('QmM0x1+1IzKX9M9HmDc7xw==')

key = b'ImSau2EGLO940cAR'
# key = 'rjBFAaHsNkKAhpoi'
print(key)
# print(b64encode(key).decode('utf-8'),"kkkkkkkkkk")

cipher = AES.new(key, AES.MODE_CBC)
ciphertext = cipher.encrypt(pad(sensitive_data, AES.block_size))

print(f"iv: {b64encode(cipher.iv).decode('utf-8')}")
print(f"ciphertext:{b64encode(ciphertext).decode('utf-8')}")
print(f"key: {b64encode(key).decode('utf-8')}")
print(key)

#Sample output
#iv: V3/oW179L1BRtRP11Nfc/w==
#ciphertext:0W6tw7CduTlymN8tOeWAL4UhCuu0ItyV7oZ7q3JWx3k=
#key: jbFlVdSLxI7kWkQTTjvoyQ==