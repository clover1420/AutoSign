import requests
import random
import time
import base64
import src.setting as url
from src.log import Log

log = Log()

# 小黑盒签到
class XiaoHeiHe():
    def __init__(self,SignToken) -> None:
        self.Xiaoheihe = SignToken['XiaoHeiHe']['cookie']
        self.imei = SignToken['XiaoHeiHe']['imei']
        self.heybox_id = SignToken['XiaoHeiHe']['heybox_id']
        self.version = SignToken['XiaoHeiHe']['version']
        self.n = self.get_nonce_str()
        self.t = int(time.time())
        #self.u = "/task/sign"

    def get_nonce_str(self,length: int = 32) -> str:
            """
            生成随机字符串
            参数:
                length: 密钥参数
            返回:
                str: 随机字符串
            """
            source = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            result = "".join(random.choice(source) for _ in range(length))
            return(result)

    def hkey(self,key):
        params={"urlpath": key, "nonce": self.n, "timestamp": self.t}
        zz = requests.get(url.XiaoHeiHe_Hkey,params=params).text
        return zz

    def params(self,key):
        p = {
            "_time":self.t,
            "hkey":self.hkey(key),
            "nonce":self.n,
            "imei":self.imei,
            "heybox_id":self.heybox_id,
            "version":self.version,
            "divice_info":"M2012K11AC",
            "x_app":"heybox",
            "channel":"heybox_xiaomi",
            "os_version":"13",
            "os_type":"Android"
        }
        return p

    def head(self):
        head = {
            "User-Agent":"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36 ApiMaxJia/1.0",
            "cookie":self.Xiaoheihe,
            "Referer":"http://api.maxjia.com/"
        }
        return head

    def b64encode(self,data: str) -> str:
        result = base64.b64encode(data.encode('utf-8')).decode('utf-8')
        return(str(result))

    def getpost(self):
        req = requests.get(
            url=url.XiaoHeiHe_News,
            params=self.params("/bbs/app/feeds/news"),
            headers=self.head()
            ).json()['result']['links'][1]['linkid']
        def click(link_id):
            head = self.params("/bbs/app/link/share/click")
            head['h_src'] = self.b64encode('news_feeds_-1')
            head['link_id'] = link_id
            head['index'] = 1
            req = requests.get(url=url.XiaoHeiHe_Click,params=head,headers=self.head()).json()['status']
            if req == "ok":
                log.info("分享成功")
                msg_req = "分享成功"
            else:
                log.info("分享失败")
                msg_req = "分享失败"
            return msg_req
        def check():
            head =  self.params("/task/shared/")
            head['h_src'] = self.b64encode('news_feeds_-1')
            head['shared_type'] = 'normal'
            req = requests.get(url=url.XiaoHeiHe_Check,params=head,headers=self.head()).json()['status']
            if req == "ok":
                log.info("检查分享成功")
                msg_req = "检查分享成功"
            else:
                log.info("检查分享失败")
                msg_req = "检查分享失败"
            return msg_req
        return click(req)+"\n"+check()

    def Sgin(self):
        if self.Xiaoheihe != "":
            try:
                req = requests.get(
                    url=url.XiaoHeiHe_SginUrl,
                    params=self.params("/task/sign/"),
                    headers=self.head()
                    ).json()
                fx = self.getpost()
                if req['status'] == "ok":
                    if req['msg'] == "":
                        log.info("小黑盒:已经签到过了")
                        return fx+"\n已经签到过了"
                    else:
                        log.info(f"小黑盒:{req['msg']}")
                        return {fx} + "\n" + req['msg']
                else:
                    log.info(f"小黑盒:签到失败 - {req['msg']}")
                    return f"{fx}\n签到失败 - {req['msg']}"   
            except Exception as e:
                log.info(f"小黑盒:出现了错误,错误信息{e}")
                return f"出现了错误,错误信息{e}"
        else:
            log.info("小黑盒:没有配置cookie")
            return "没有配置cookie"

# 交易猫签到
class JiaoYiMao():
    def __init__(self,SignToken) -> None:
        self.jiaoyimao = SignToken['JiaoYiMao']['cookie']

    def Sgin(self):
        if self.jiaoyimao != "":
            head = {
                "user-agent":"jym_mobile (Linux; U; Android12; zh_CN; M2012K11AC; Build/SKQ1.220213.001; fca7d8fc-03b5-4fea-97e6-94173844b374; 1080x2400) com.jym.mall/206/JYN_548/7.0.2 AliApp(JYM/7.0.2) UT4Aplus/0.2.29; density/2.7; app_id/23072786;  WindVane/8.5.0; utdid/YH2ygxDifiEDAA6wMV75K10e; umid_token/7+9LGztLOiq8MTWA+l8fZZQW+RjvBE56; oaid/9933af2363237087;",
                "referer":url.JiaoYiMao_Referer,
                "x-csrf-token":"HT-x5YUi3IF7iyVDXY6FBc6g",
                "x-requested-with":"com.jym.mall",
                "cookie":self.jiaoyimao
            }
            try:
                zz = requests.get(url=url.JiaoYiMao_SginUrl,headers=head).json()
                if zz['success']:
                    rep = requests.get(url=url.JiaoYiMao_Url,headers=head).json()
                    if rep['stateCode'] == 200:
                        Integral = rep['data']['amountLeft']
                    else:
                        Integral = "获取积分失败"
                    
                    log.info(f"交易猫:签到成功 - 现有积分{Integral}")
                    return f"签到成功 - 现有积分{Integral}"
                else:
                    
                    log.info(f"交易猫:签到失败 - 已经签到了")
                    return f"签到失败 - 已经签到了"
            except Exception as e:
                log.info("交易猫:cookie可能已过期，或出现了错误")
                return "cookie可能已过期，或出现了错误"
        else:
            log.info("交易猫:没有配置cookie")
            return "没有配置cookie"

# 网易云游戏签到
class wyyyx():
    def __init__(self,SignToken) -> None:
        self.wyyyx_cookie = SignToken['wyyyx']['cookie']

    def Sgin(self):
        url='https://n.cg.163.com/api/v2/sign-today'
        header={
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5',
            'Authorization': self.wyyyx_cookie,
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Host': 'n.cg.163.com',
            'Origin': 'https://cg.163.com',
            'Referer': 'https://cg.163.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'X-Platform': '0'
        }
        res = requests.post(url=url,headers=header).status_code
        if res == 200:
            log.info("网易云游戏:签到成功")
            return "签到成功"
        else:
            log.info("网易云游戏:签到失败或已签到")
            return "签到失败或已签到"
        