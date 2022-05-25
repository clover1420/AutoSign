from os import rename
import requests
import random
import time
from src.log import Log

log = Log()

class gtfed():
    """好游快爆签到
    """
    url = 'https://huodong3.3839.com/n/hykb/grow/ajax.php'
    def __init__(self,SignToken) -> None:
        self.gtfed = SignToken['gtfed']['cookie']
        self.head = {
            "User-Agent":"Mozilla/5.0 (Linux; Android 7.0; Meizu S6 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.110 Mobile Safari/537.36Androidkb/1.5.5.305(android;Meizu S6;7.0;720x1374;4G);@4399_sykb_android_activity@",
            "Origin":"https://huodong3.3839.com",
            "X-Requested-With":"XMLHttpRequest",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Referer":"https://huodong3.3839.com/n/hykb/grow/index.php",
	    }
        
    def Sign(self):
        if self.gtfed != "":
            zz = requests.post(url=self.url,data=self.gtfed,headers=self.head).json()
            if zz['key'] == 'ok':
                if zz['csd_jdt'] == "100%":
                    log.info("好游快爆:爆米进度已满")
                    return "好游快爆:爆米进度已满"
                else:
                    log.info("好游快爆:签到成功")
                    return "好游快爆:签到成功"
            else:
                log.info(f"好游快爆:{zz['info']}")
                return f"好游快爆:{zz['info']}"
        else:
            log.info("好游快爆:没有配置cookie")
            return "好游快爆:没有配置cookie"
            
#MIUI 历史版本签到
class Miui():
    """MIUI 历史版本签到
    """
    LoginUrl = "https://miuiver.com/wp-content/plugins/erphplogin//action/login.php"
    SignUrl = "https://miuiver.com/wp-admin/admin-ajax.php"
    def __init__(self,SignToken) -> None:
        self.switch = SignToken['MiUI']['switch']
        self.user = SignToken['MiUI']['user']
        self.password = SignToken['MiUI']['password']
        self.head = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01'
        }
    #登录
    def Login(self):
        datas = {
            'log':self.user,
            'pwd':self.password,
            'action': 'mobantu_login'
        }
        response = requests.post(url=self.LoginUrl,data=datas,headers=self.head)
        if response.text == '1':
            log.info("MIUI历史版本:登录成功")
            if response.text.__eq__(1):
                cookies = response.cookies
                log.info("MIUI历史版本:cookies获取成功")
            else:
                cookies = "没有获取到cookie"
                log.info("MIUI历史版本:没有获取到cookie")
            return cookies
        else:
            log.info("MIUI历史版本:登录失败,账号或密码错误")
    #签到
    def Sign(self):
        datas = {
            'action': 'epd_checkin'
        }
        if self.user != "" and self.password != "":
            cookies = self.Login()
            if cookies == None:
                pass
            else:
                response = requests.post(url=self.SignUrl,data=datas,headers=self.head,cookies=cookies).json()
                if response['status'] == 200:
                    log.info("MIUI历史版本:" + "签到成功积分+1")
                    return "MIUI历史版本:" + "签到成功积分+1"
                else:
                    log.info("MIUI历史版本:" + response["msg"])
                    return "MIUI历史版本:" + response["msg"]
        else:
            log.info("MIUI历史版本:账号或密码为空")
            return "MIUI历史版本:账号或密码为空"

# 小黑盒签到
class XiaoHeiHe():
    def __init__(self,SignToken) -> None:
        self.Xiaoheihe = SignToken['XiaoHeiHe']['cookie']
        self.imei = SignToken['XiaoHeiHe']['imei']
        self.n = self.get_nonce_str()
        self.t = int(time.time())
        self.u = "/task/sign"

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

    # 感谢 https://github.com/chr233 的hkey算法接口
    def hkey(self):
        url = "http://146.56.234.178:8077/encode"
        params={"urlpath": self.u, "nonce": self.n, "timestamp": self.t}
        zz = requests.get(url,params=params).text
        return zz
    
    def Sgin(self):
        if self.Xiaoheihe != "":
            try:
                url = "https://api.xiaoheihe.cn/task/sign/"
                p = {
                    "_time":self.t,
                    "hkey":self.hkey(),
                    "nonce":self.n,
                    "imei":self.imei,
                    "heybox_id":"15083711",
                    "version":"1.3.221",
                    "divice_info":"M2012K11AC",
                    "x_app":"heybox",
                    "channel":"heybox_xiaomi",
                    "os_version":"12",
                    "os_type":"Android"
                }
                head = {
                    "User-Agent":"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36 ApiMaxJia/1.0",
                    "cookie":self.Xiaoheihe,
                    "Referer":"http://api.maxjia.com/"
                }
                req = requests.get(url=url,params=p,headers=head).json()
                if req['status'] == "ok":
                    if req['msg'] == "":
                        log.info("小黑盒:已经签到过了")
                        return "小黑盒:已经签到过了"
                    else:
                        log.info(f"小黑盒:{req['msg']}")
                        return f"小黑盒:{req['msg']}"
                else:
                    log.info("小黑盒:签到失败")
                    return "小黑盒:签到失败"
            except Exception as e:
                log.info(f"小黑盒:出现了错误,错误信息{e}")
        else:
            log.info("小黑盒:没有配置cookie")
            return "小黑盒:没有配置cookie"

# 交易猫签到
class JiaoYiMao():
    def __init__(self,SignToken) -> None:
        self.jiaoyimao = SignToken['JiaoYiMao']['cookie']
        self.url = "https://m.jiaoyimao.com/api2/account/integration/getMyIntegration"

    def Sgin(self):
        if self.jiaoyimao != "":
            head = {
                "user-agent":"jym_mobile (Linux; U; Android12; zh_CN; M2012K11AC; Build/SKQ1.220213.001; fca7d8fc-03b5-4fea-97e6-94173844b374; 1080x2400) com.jym.mall/206/JYN_548/7.0.2 AliApp(JYM/7.0.2) UT4Aplus/0.2.29; density/2.7; app_id/23072786;  WindVane/8.5.0; utdid/YH2ygxDifiEDAA6wMV75K10e; umid_token/7+9LGztLOiq8MTWA+l8fZZQW+RjvBE56; oaid/9933af2363237087;",
                "referer":"https://m.jiaoyimao.com/account/integration/center?spm=gcmall.home2022.topshortcut.0",
                "x-csrf-token":"HT-x5YUi3IF7iyVDXY6FBc6g",
                "x-requested-with":"com.jym.mall",
                "cookie":self.jiaoyimao
            }
            zz = requests.get(url=self.url,headers=head).json()
            if zz['stateCode'] == 200:
                data = f"交易猫:签到成功 - 现有积分{zz['data']['amountLeft']}"
                log.info(data)
                return data
            else:
                data = f"交易猫:签到失败 - {zz}"
                log.info(data)
                return data
        else:
            log.info("交易猫:没有配置cookie")
            return "交易猫:没有配置cookie"
