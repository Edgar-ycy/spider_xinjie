import random
from Cryptodome.Cipher import AES
from base64 import b64encode
from Cryptodome.Util.Padding import pad


def random_str(num):
    aes_chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678'
    retstr = ''
    for i in range(num):
        retstr += random.choice(aes_chars)

    return retstr


def get_aes_string(data:str,key0:str,iv0:str):
    # sensitive_data, iv, key = 'rjBFAaHsNkKAhpoi'.encode("utf-8"), 'rjBFAaHsNkKAhpoi'.encode(
    #     "utf-8"), 'rjBFAaHsNkKAhpoi'.encode("utf-8")
    data = data.encode("utf-8")
    key = key0.encode("utf-8")
    iv = iv0.encode("utf-8")

    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))

    # print(f"iv: {b64encode(cipher.iv).decode('utf-8')}")
    # print(f"ciphertext:{b64encode(ciphertext).decode()}")
    # print(f"key: {b64encode(key).decode('utf-8')}")

    return b64encode(ciphertext).decode()  # 结果


def encrypt_aes(data,aes_key):
    encrypted = get_aes_string(random_str(64)+data,aes_key,random_str(16))

    return encrypted

def encrypt_password(pwd0):
    pwd1 = encrypt_aes(pwd0,pwdDefaultEncryptSalt)

    # passwordEncrypt = pwd1
    return pwd1




if __name__ == '__main__':
    print(get_aes_string('rjBFAaHsNkKAhpoi','rjBFAaHsNkKAhpoi','rjBFAaHsNkKAhpoi'))

# roA9pfhObBYgTsn1pEMva60N3fQ3XbLUTNPU4ek3vBZMTKq8C2YeF1yrn5RhR91L0JJsffZAP8b3fQGrPvNIc/ofKkyH1vrslYJFq8gexT8=
# fjcAai14SfKIsyIf+ACfDqXAUvtEuc2ONRj+mA+h0dpGCNTsD/z+RzuqEzZdH0SC6kSpx7muq8IuSxnyka23a9ar1FkvxYZxn3pnmhROltw=


# 三个一样都是'rjBFAaHsNkKAhpoi'

# ylawF33IbdytvuTjJYB7Wd+XpsOUSruMFFjr6hFZgi0=
# ylawF33IbdytvuTjJYB7Wd+XpsOUSruMFFjr6hFZgi0=
# ylawF33IbdytvuTjJYB7Wd+XpsOUSruMFFjr6hFZgi0=
