import random

from Cryptodome.Cipher import AES
from binascii import b2a_hex, a2b_hex
from Cryptodome import Random
from base64 import b64encode

from Cryptodome.Util.Padding import pad
from Cryptodome.Random import get_random_bytes


def random_str(num):
    aes_chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678'
    retstr = ''
    for i in range(num):
        retstr += random.choice(aes_chars)

    return retstr


if __name__ == '__main__':
    aesKey = 'rjBFAaHsNkKAhpoi'.encode('utf-8')
    iv = random_str(16)
    data = 'Ycy125698'
    data = random_str(64)+data
    # print(iv,data)

    sensitive_data = data.encode("utf-8")
    sensitive_data = aesKey

    # key = get_random_bytes(16)  # must be 16, 24 or 32 bytes long
    key = b'rjBFAaHsNkKAhpoi'
    key = 'rjBFAaHsNkKAhpoi'.encode("utf-8")

    # iv = 'b2324rJKZn75iwG8'

    iv = bytes(iv, encoding="utf8")
    print(iv,',,,,,,,,,,,,,,,,,')

    iv = aesKey
    cipher = AES.new(key=key,mode=AES.MODE_CBC, iv=iv)
    ciphertext = cipher.encrypt(pad(sensitive_data, AES.block_size))

    # print(f"iv: {b64encode(cipher.iv).decode('utf-8')}")
    print(f"ciphertext:{b64encode(ciphertext).decode()}")
    # print(f"key: {b64encode(key).decode('utf-8')}")


# roA9pfhObBYgTsn1pEMva60N3fQ3XbLUTNPU4ek3vBZMTKq8C2YeF1yrn5RhR91L0JJsffZAP8b3fQGrPvNIc/ofKkyH1vrslYJFq8gexT8=
# fjcAai14SfKIsyIf+ACfDqXAUvtEuc2ONRj+mA+h0dpGCNTsD/z+RzuqEzZdH0SC6kSpx7muq8IuSxnyka23a9ar1FkvxYZxn3pnmhROltw=
# cRqUDHXzToWIITOsuOYptcTDWzonKd1qRmEp1CQS/QPm+wlaLAabPQAMFQlEA7uvrPWy4q4SHOVKFmm17KWbzjSu6O6mSsPAX+UoGW8ZxaE=
# dNHdD1tmOvyVi03jj9FGvtp9BjWCButpDGkRGILjWhdlqMPawRWyKe9Pvv2JsLV8a+Fm79xprzSZH2ybWrsGZxBiNwnQeVYmYJhbgqq7iYc=
# A0B8aBOY2krzKpVsxh7B1NeD65PQL3QAxDFLH5V+d3kqOqU96NPz10j3//X3JeSuqKjrrsZio1/g2qmsEt6v1pVfK3Z7TRSaZHpSNXg83Ro=
# vngCpbmzRyYtvgc809Vnu0s/fCbf8CygtazCYN2E2RuXRgz6VZLGWtbh4w9Q2tFqVL8l45WRVRlSovpz6JsckUCJNu1xb99nxUXkc4UDEzs=
# WM014w6jxm0ZD4qE6C60MIRmcCd+27QvE0tUhM8oxr/YT6RXtppir+NmzB8BXIex/xkSYXMgFSE4dtfVyMEXa2IAf8rv9/Zj71rmvqQADww=
# PgFw1qNpauPVfOOeJPh9OqSPgHsGkNaw9n8NBDs2gARMswUp61cpgIBt6CUvvdhEtWJUtnhirVqcvpSjf/KLop+lBf/5sf1gGOevFJxmTNw=




# 三个一样都是'rjBFAaHsNkKAhpoi'

# ylawF33IbdytvuTjJYB7Wd+XpsOUSruMFFjr6hFZgi0=
# ylawF33IbdytvuTjJYB7Wd+XpsOUSruMFFjr6hFZgi0=
# ylawF33IbdytvuTjJYB7Wd+XpsOUSruMFFjr6hFZgi0=

