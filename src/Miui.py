import src.setting as url
import requests
from src.log import Log

log = Log()

#MIUI 历史版本签到
class Miui():
    """MIUI 历史版本签到
    """
    def __init__(self,SignToken) -> None:
        self.user = SignToken['username']
        self.password = SignToken['password']
        self.head = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'Origin':'https://miuiver.com/',
            'Referer':'https://miuiver.com/',
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
        response = requests.post(url=url.Miui_LoginUrl,data=datas,headers=self.head)
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
                response = requests.post(url=url.Miui_SginUrl,data=datas,headers=self.head,cookies=cookies).json()
                if response['status'] == 200:
                    log.info("MIUI历史版本:签到成功积分+1")
                    return "签到成功积分+1"
                else:
                    log.info("MIUI历史版本:" + response["msg"])
                    return response["msg"]
        else:
            log.info("MIUI历史版本:账号或密码为空")
            return "账号或密码为空"