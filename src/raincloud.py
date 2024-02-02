import requests
from src.log import Log

log = Log()

class RainCloud():
    def __init__(self, config) -> None:
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
            "X-Api-Key": config['apikey'],
            "content-type": "application/json"
        }
    
    def get_user_info(self):
        user_info_url = "https://api.v2.rainyun.com/user/"
        rsp = requests.get(user_info_url, headers=self.headers).json()
        if rsp['code'] == 200:
            return rsp['data']['Points']
        else:
            log.info(f"雨云：获取用户信息失败，请检查apikey是否正确")
            log.info(f"雨云：返回信息：{rsp}")
            return 0
    
    def sgin(self):
        sginurl = "https://api.v2.rainyun.com/user/reward/tasks"
        data = {"task_name": "每日签到", "verifyCode": ""}
        rsp = requests.post(sginurl, json=data, headers=self.headers).json()
        if rsp['code'] == 200:
            if rsp['data'] == "ok":
                info = f"雨云：签到成功，积分+300，现有积分{self.get_user_info()+300}"
                log.info(info)
                return info
        elif rsp['code'] == 30011:
            info = f"雨云：今日已签到，现有积分{self.get_user_info()}"
            log.info(info)
            return info
        else:
            info = f"雨云：签到失败，请检查apikey是否正确"
            log.info(info)
            return info