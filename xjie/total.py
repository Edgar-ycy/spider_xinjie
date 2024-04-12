import re
import time
import random
import requests
from urllib import parse
from fake_useragent import UserAgent
from lxml import etree

from Cryptodome.Cipher import AES
from binascii import b2a_hex, a2b_hex
from Cryptodome import Random
from base64 import b64encode

from Cryptodome.Util.Padding import pad
from Cryptodome.Random import get_random_bytes

ua = str(UserAgent().random)


# ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'


def random_str(num):
    aes_chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678'
    retstr = ''
    for i in range(num):
        retstr += random.choice(aes_chars)

    return retstr


def get_aes_string(data: str, key0: str, iv0: str):
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


def encrypt_aes(data, aes_key):
    encrypted = get_aes_string(random_str(64) + data, aes_key, random_str(16))

    return encrypted


def encrypt_password(pwd0):
    pwd1 = encrypt_aes(pwd0, pwdDefaultEncryptSalt)

    # passwordEncrypt = pwd1
    return pwd1


class Xjie:
    def __init__(self):
        self.aesKey = 'rjBFAaHsNkKAhpoi'.encode('utf-8')

        self.url0 = 'http://authserver.xjie.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xjie.edu.cn%2Fjsxsd%2F'
        self.url1 = 'http://jwxt.xjie.edu.cn/jsxsd/framework/xsMain.jsp'
        self.regex_salt = re.compile('pwdDefaultEncryptSalt = "(.*?)";', re.S)
        self.regex_lt = re.compile('name="lt" value="(.*?)"', re.S)
        self.regex_dllt = re.compile('name="dllt" value="(.*?)"', re.S)
        self.regex_execution = re.compile('name="execution" value="(.*?)"', re.S)
        self.regex__eventId = re.compile('name="_eventId" value="(.*?)"', re.S)
        self.regex_rmShown = re.compile('name="rmShown" value="(.*?)"', re.S)

        self.sess = requests.session()

    def encrypt_password(self, pwd0):
        pwd1 = encrypt_aes(pwd0, self.salt)

        # passwordEncrypt = pwd1
        return pwd1

    def parse_html1(self):
        self.headers01 = {
            'User-Agent': ua,
            'Host': 'authserver.xjie.edu.cn',
        }
        html = self.sess.get(self.url0, headers=self.headers01)
        print(html.status_code, "第一次get")
        html = html.content.decode()

        self.salt = self.regex_salt.findall(html)[0]
        self.lt = self.regex_lt.findall(html)[0]
        self.dllt = self.regex_dllt.findall(html)[0]。
        self.execution = self.regex_execution.findall(html)[0]
        self._eventId = self.regex__eventId.findall(html)[0]
        self.rmShown = self.regex_rmShown.findall(html)[0]

        with open("first.html", 'w') as fw:
            fw.write(html)

        print(self.salt, self.lt, self.dllt, self.execution, self._eventId, self.rmShown)
        # time.sleep(1)
        self.passwd_ = self.encrypt_password('YCY125698')
        time.sleep(1)
        return

    def parse_html2(self):
        self.parse_html1()

        self.headers02 = {
            'User-Agent': ua,
            'Referer': 'http://authserver.xjie.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xjie.edu.cn%2Fjsxsd%2F',
            'Host': 'authserver.xjie.edu.cn',
            'Origin': 'http://authserver.xjie.edu.cn',
        }

        self.data1 = {
            'username': '2019210918',
            'password': self.passwd_,
            'lt': self.lt,
            'dllt': self.dllt,
            'execution': self.execution,
            '_eventId': self._eventId,
            'rmShown': self.rmShown,
        }
        resp = self.sess.post(self.url0, data=self.data1, headers=self.headers02, allow_redirects=False)
        print(resp.history)
        print(resp.status_code, '第二次POST')
        print("2222222222222", resp.headers, '2222222222222')

        html = resp.content.decode()

        with open('second.html', 'w') as fw:
            fw.write(html)
        # self.passwd_ = self.mima()
        time.sleep(1)
        if resp.status_code == 302:
            # return resp.headers['Location']
            return resp.headers.get('Location')


    def parse_html3(self):
        self.url3 = self.parse_html2()
        self.headers03 = {
            'User-Agent': ua,
            'Host': 'authserver.xjie.edu.cn',
            'Referer': 'http://authserver.xjie.edu.cn/',
        }
        resp = self.sess.get(self.url3, headers=self.headers03, allow_redirects=False)
        print(resp.status_code, "第三次get")
        print(resp.headers, '第三次的headers')
        html = resp.content.decode()

        with open("third.html", 'w') as fw:
            fw.write(html)
        # time.sleep(1)

        if resp.status_code == 302:
            time.sleep(1)
            return resp.headers.get('Set-Cookie'), resp.headers.get('Location')

    def parse_html4(self):
        Set_Cookie, self.url4 = self.parse_html3()

        cookie_regex = re.compile('(.*?)Path=/jsxsd; HttpOnly, (.*?); path=/')
        cookie_apart = cookie_regex.findall(Set_Cookie)[0]
        self.cookie = cookie_apart[0] + cookie_apart[1]

        print(self.cookie, '4444444444444444444444444444444')
        self.headers04 = {
            'User-Agent': ua,
            'Host': 'jwxt.xjie.edu.cn',
            'Referer': 'http://authserver.xjie.edu.cn/',
            'Cookie': self.cookie,
        }
        resp = self.sess.get(self.url4, headers=self.headers04, allow_redirects=False)
        print(resp.status_code, "第四次get")
        print(resp.headers, '第四次的headers')
        html = resp.content.decode()

        with open("forth.html", 'w') as fw:
            fw.write(html)
        # time.sleep(1)
        time.sleep(1)
        if resp.status_code == 302:
            return resp.headers.get('Location')

    def parse_html5(self):

        self.url5 = self.parse_html4()

        self.headers05 = {
            'User-Agent': ua,
            'Host': 'jwxt.xjie.edu.cn',
            'Referer': 'http://authserver.xjie.edu.cn/',
            'Cookie': self.cookie,
        }
        html = self.sess.get(self.url5, headers=self.headers05, allow_redirects=False)
        print(html.status_code, "第五次get")
        print(html.headers, '第五次的headers')
        html = html.content.decode()
        time.sleep(1)
        with open("fifth.html", 'w') as fw:
            fw.write(html)
        # time.sleep(1)


    def schedule_html(self):

        self.schedule_url = 'http://jwxt.xjie.edu.cn/jsxsd/xskb/xskb_list.do'

        self.schedule_headers = {
            'User-Agent': ua,
            'Host': 'jwxt.xjie.edu.cn',
            'Referer': 'http://jwxt.xjie.edu.cn/jsxsd/framework/xsMain.jsp',
            'Cookie': self.cookie,
        }
        html = self.sess.get(self.schedule_url, headers=self.schedule_headers, allow_redirects=False)
        print(html.status_code, "第六次课表get")
        print(html.headers, '第六次课表headers')
        html = html.content.decode()

        with open("schedule.html", 'w') as fw:
            fw.write(html)
        time.sleep(1)

    def save_data(self, html):
        pass

    def run(self):
        # self.parse_html2()
        # self.parse_html3()
        # self.parse_html4()
        self.parse_html5()
        self.schedule_html()


if __name__ == '__main__':
    spider = Xjie()
    spider.run()
