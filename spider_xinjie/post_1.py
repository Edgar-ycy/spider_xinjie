import requests

url = 'http://authserver.xjie.edu.cn/authserver/login?service=http://jwxt.xjie.edu.cn/jsxsd/'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '283',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'route=7fba8780761dc06ef073ed6406572753; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; JSESSIONID=lVKEwL3CLMVc72DrHyTkpDEwXtAhzJfmVwoE7U3Ck4FOJtmlew8D!1396484138',
    'Host': 'authserver.spider_xinjie.edu.cn',
    'Origin': 'http://authserver.xjie.edu.cn',
    'Referer': 'http://authserver.xjie.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xjie.edu.cn%2Fjsxsd%2F',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',
}
data = {
    'username': '2019210918',
    'password': 'WM014w6jxm0ZD4qE6C60MIRmcCd%2B27QvE0tUhM8oxr%2FYT6RXtppir%2BNmzB8BXIex%2FxkSYXMgFSE4dtfVyMEXa2IAf8rv9%2FZj71rmvqQADww%3D',
    'lt': 'LT-652809-uQQ0NDvAOci9bPFbwCbqfT0uackpAd1664379567554-aSqS-cas',
    'dllt': 'userNamePasswordLogin',
    'execution': 'e1s1',
    '_eventId': 'submit',
    'rmShown': '1',

}

resp = requests.post(url=url, headers=headers, data=data)

print(resp.status_code)
