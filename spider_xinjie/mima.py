from Cryptodome.Cipher import AES
from binascii import b2a_hex, a2b_hex
from Cryptodome import Random

class PrpCrypt(object):

  def __init__(self, key):
    self.key = key.encode('utf-8')
    self.mode = AES.MODE_CBC
    self.iv = Random.new().read(AES.block_size)

  # 加密函数，如果text不足16位就用空格补足为16位，
  # 如果大于16当时不是16的倍数，那就补足为16的倍数。
  def encrypt(self, text):
    text = text.encode('utf-8')

    cryptor = AES.new(self.key, self.mode,self.iv)
    # 这里密钥key 长度必须为16（AES-128）,
    # 24（AES-192）,或者32 （AES-256）Bytes 长度
    # 目前AES-128 足够目前使用
    length = 16
    count = len(text)
    if count < length:
      add = (length - count)
      # \0 backspace
      # text = text + ('\0' * add)
      text = text + ('\0' * add).encode('utf-8')
    elif count > length:
      add = (length - (count % length))
      # text = text + ('\0' * add)
      text = text + ('\0' * add).encode('utf-8')
    self.ciphertext = cryptor.encrypt(text)
    # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
    # 所以这里统一把加密后的字符串转化为16进制字符串
    return b2a_hex(self.ciphertext)

  # 解密后，去掉补足的空格用strip() 去掉
  def decrypt(self, text):
    cryptor = AES.new(self.key, self.mode, self.iv)
    plain_text = cryptor.decrypt(a2b_hex(text))
    # return plain_text.rstrip('\0')
    return bytes.decode(plain_text).rstrip('\0')


if __name__ == '__main__':
  pc = PrpCrypt('0CoJUm6Qyw8W8jud') # 初始化密钥
  data = input("请输入待加密数据：")#
  e = pc.encrypt(data) # 加密
  d = pc.decrypt(e).encode() # 解密
  print("加密:", e)
  print("解密:", d)