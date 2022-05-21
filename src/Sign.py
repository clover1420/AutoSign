import requests,logging
from src.log import Log

log = Log()
class gtfed():
    """好游快报签到
    """
    url = 'https://huodong3.3839.com/n/hykb/grow/ajax.php'
    def __init__(self,SignToken) -> None:
        self.gtfed = SignToken['gtfed']
        self.head = {
            "User-Agent":"Mozilla/5.0 (Linux; Android 7.0; Meizu S6 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.110 Mobile Safari/537.36Androidkb/1.5.5.305(android;Meizu S6;7.0;720x1374;4G);@4399_sykb_android_activity@",
            "Origin":"https://huodong3.3839.com",
            "X-Requested-With":"XMLHttpRequest",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Referer":"https://huodong3.3839.com/n/hykb/grow/index.php",
	    }
        self.data = f'ac=Watering&r=0.1399304193190738&scookie={self.gtfed}'
        
    def qd(self):
        zz = requests.post(url=self.url,data=self.data,headers=self.head).json()
        if zz['key'] == 'Ok':
            if zz['csd_jdt'] == "100%":
                pass
            else:
                log.info("好游快报:签到成功")
                return "好游快报:签到成功"
        else:
            log.info(f"好游快报:{zz['info']}")
            return f"好游快报:{zz['info']}"
#MIUI 历史版本签到
class Miui():
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