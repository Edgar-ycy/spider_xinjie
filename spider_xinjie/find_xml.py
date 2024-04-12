
import re

with open('yuanma.html',encoding="utf-8") as fr:
    html = fr.read()

p = re.compile('pwdDefaultEncryptSalt = "(.*?)";',re.S)


print(p.findall(html))