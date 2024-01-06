import re
import time
import requests
import rsa
import base64
import hashlib
from src.log import Log

log = Log()

# 天翼云盘
# 使用了开源项目https://github.com/xtyuns/cloud189app-action
class Cloud():
    def __init__(self,config) -> None:
        self.username = config['username']
        self.password = config['password']
        self.s = requests.Session()

    def int2char(self, a):
        BI_RM = list("0123456789abcdefghijklmnopqrstuvwxyz")
        return BI_RM[a]

    def b64tohex(self, a):
        B64MAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        d = ""
        e = 0
        c = 0
        for i in range(len(a)):
            if list(a)[i] != "=":
                v = B64MAP.index(list(a)[i])
                if e == 0:
                    e = 1
                    d += self.int2char(v >> 2)
                    c = 3 & v
                elif e == 1:
                    e = 2
                    d += self.int2char(c << 2 | v >> 4)
                    c = 15 & v
                elif e == 2:
                    e = 3
                    d += self.int2char(c)
                    d += self.int2char(v >> 2)
                    c = 3 & v
                else:
                    e = 0
                    d += self.int2char(c << 2 | v >> 4)
                    d += self.int2char(15 & v)
        if e == 1:
            d += self.int2char(c << 2)
        return d

    def rsa_encode(self, j_rsakey, string):
        rsa_key = f"-----BEGIN PUBLIC KEY-----\n{j_rsakey}\n-----END PUBLIC KEY-----"
        pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(rsa_key.encode())
        result = self.b64tohex((base64.b64encode(rsa.encrypt(f'{string}'.encode(), pubkey))).decode())
        return result
    
    # 登录函数
    def login(self, username, password):
        urlToken = "https://m.cloud.189.cn/udb/udb_login.jsp?pageId=1&pageKey=default&clientType=wap&redirectURL=https://m.cloud.189.cn/zhuanti/2021/shakeLottery/index.html"
        r = self.s.get(urlToken)
        pattern = r"https?://[^\s'\"]+"  # 匹配以http或https开头的url
        match = re.search(pattern, r.text)  # 在文本中搜索匹配
        if match:  # 如果找到匹配
            url = match.group()  # 获取匹配的字符串
        else:  # 如果没有找到匹配
            log.info("没有找到url")
            return None

        r = self.s.get(url)
        pattern = r"<a id=\"j-tab-login-link\"[^>]*href=\"([^\"]+)\""  # 匹配id为j-tab-login-link的a标签，并捕获href引号内的内容
        match = re.search(pattern, r.text)  # 在文本中搜索匹配
        if match:  # 如果找到匹配
            href = match.group(1)  # 获取捕获的内容
        else:  # 如果没有找到匹配
            log.info("没有找到href链接")
            return None

        r = self.s.get(href)
        captchaToken = re.findall(r"captchaToken' value='(.+?)'", r.text)[0]
        lt = re.findall(r'lt = "(.+?)"', r.text)[0]
        returnUrl = re.findall(r"returnUrl= '(.+?)'", r.text)[0]
        paramId = re.findall(r'paramId = "(.+?)"', r.text)[0]
        j_rsakey = re.findall(r'j_rsaKey" value="(\S+)"', r.text, re.M)[0]
        self.s.headers.update({"lt": lt})

        username = self.rsa_encode(j_rsakey, username)
        password = self.rsa_encode(j_rsakey, password)
        url = "https://open.e.189.cn/api/logbox/oauth2/loginSubmit.do"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/76.0',
            'Referer': 'https://open.e.189.cn/',
        }
        data = {
            "appKey": "cloud",
            "accountType": '01',
            "userName": f"{{RSA}}{username}",
            "password": f"{{RSA}}{password}",
            "validateCode": "",
            "captchaToken": captchaToken,
            "returnUrl": returnUrl,
            "mailSuffix": "@189.cn",
            "paramId": paramId
        }
        r = self.s.post(url, data=data, headers=headers, timeout=5)
        if r.json()['result'] == 0:
            log.info(r.json()['msg'])
        else:
            log.info(r.json()['msg'])
        redirect_url = r.json()['toUrl']
        r = self.s.get(redirect_url)
        return self.s
    
    # 签到函数
    def sgin(self):
        s = self.login(self.username, self.password)
        if not s:
            log.info("登录失败")
        rand = str(round(time.time() * 1000))
        surl = f'https://api.cloud.189.cn/mkt/userSign.action?rand={rand}&clientType=TELEANDROID&version=8.6.3&model=SM-G930K'
        url = f'https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action?taskId=TASK_SIGNIN&activityId=ACT_SIGNIN'
        url2 = f'https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action?taskId=TASK_SIGNIN_PHOTOS&activityId=ACT_SIGNIN'
        url3 = f'https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action?taskId=TASK_2022_FLDFS_KJ&activityId=ACT_SIGNIN'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G930K Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Ecloud/8.6.3 Android/22 clientId/355325117317828 clientModel/SM-G930K imsi/460071114317824 clientChannelId/qq proVersion/1.0.6',
            "Referer": "https://m.cloud.189.cn/zhuanti/2016/sign/index.jsp?albumBackupOpened=1",
            "Host": "m.cloud.189.cn",
            "Accept-Encoding": "gzip, deflate",
        }
        # 签到
        response = s.get(surl, headers=headers).json()
        netdiskBonus = response['netdiskBonus']
        if not response['isSign']:
            log.info(f"天翼云盘:签到成功，获得：{netdiskBonus}M空间")
            message =  f"签到成功，获得：{netdiskBonus}M空间"
        else:
            log.info(f"天翼云盘:已经签到过了，获得：{netdiskBonus}M空间")
            message =  f"已经签到过了，获得：{netdiskBonus}M空间"

        # 第一次抽奖
        response = s.get(url, headers=headers).json()
        try:
            if "errorCode" in response:
                log.info("天翼云盘:第一次抽奖-没有抽奖次数")
                message += "\n第一次抽奖-没有抽奖次数"
            else:
                log.info(f"天翼云盘:第一次抽奖获得{response['prizeName']}")
                message += f"\n第一次抽奖获得{response['prizeName']}"
        except Exception as er:
            log.info(f"天翼云盘:第一次抽奖出现了错误:{er}")
            message += f"\n第一次抽奖出现了错误:{er}"

        # 第二次抽奖
        response = s.get(url2, headers=headers).json()
        try:
            if "errorCode" in response:
                log.info("天翼云盘:第二次抽奖-没有抽奖次数")
                message += "\n第二次抽奖-没有抽奖次数"
            else:
                log.info(f"天翼云盘:第二次抽奖获得{response['prizeName']}")
                message += f"\n第二次抽奖获得{response['prizeName']}"
        except Exception as er:
            log.info(f"天翼云盘:第二次抽奖出现了错误:{er}")
            message += f"\n第二次抽奖出现了错误:{er}"
        return message
