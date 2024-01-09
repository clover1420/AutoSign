import requests
from src.log import Log


log = Log()

class Aliyundrive:
    def __init__(self, coofig):
        self.token = self.get_access_token(coofig['token'])
        self.headers = {
                "Content-Type": "application/json",
                "Authorization": self.token,
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 D/C501C6D2-FAF6-4DA8-B65B-7B8B392901EB"
            }

    def get_access_token(self,token):
        access_token = ''
        try:
            url = "https://auth.aliyundrive.com/v2/account/token"

            data_dict = {
                "refresh_token": token,
                "grant_type": "refresh_token"
            }
            headers = {
                "accept": "application/json, text/plain, */*",
                "accept-language": "zh-CN,zh;q=0.9",
                "cache-control": "no-cache",
                "content-type": "application/json;charset=UTF-8",
                "origin": "https://www.aliyundrive.com",
                "pragma": "no-cache",
                "referer": "https://www.aliyundrive.com/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            }

            resp = requests.post(url, json=data_dict, headers=headers).json()

            token = {}
            token['access_token'] = resp['access_token']
            access_token = token['access_token']
        except Exception as e:
            log.error(f"获取异常:{e}")

        return access_token
    

    # 获取奖励
    def get_reward(self, day):
        try:
            url = 'https://member.aliyundrive.com/v1/activity/sign_in_reward'
            body = {
                'signInDay': day
            }
            rep = requests.post(url, json=body, headers=self.headers).json()
            return rep['success']
        except Exception as e:
            log.error(f"获取签到奖励异常={e}")
            return False
    

    # 签到
    def sign_in(self):
        url = "https://member.aliyundrive.com/v2/activity/sign_in_info"
        #url = 'https://member.aliyundrive.com/v2/activity/sign_in_list'
        #url = 'https://member.aliyundrive.com/v1/activity/sign_in_list'
        body = {}
        resp = requests.post(url, json=body, headers=self.headers).json()
        return resp
    
    # 是否领取了奖励
    def isReward(self):
        url = "https://member.aliyundrive.com/v1/activity/sign_in_goods"
        body = {}
        resp = requests.post(url, json=body, headers=self.headers).json()
        return resp['result']['isReward']
    

    def sgin(self):
        # 签到
        resp = self.sign_in()

        reward_name = resp['result']['rewards'][0]['name']
        sgin_day = resp['result']['day']
        if resp['success']:
            if resp['result']['isSignIn']:
                if self.get_reward(resp['result']['signInDay']):
                    content = f"✅打卡第{sgin_day}天，获得奖励：**[{reward_name}]**"
                    log.info(content)
                else:
                    content = f"✅打卡第{sgin_day}天，获得奖励：**[ 失败 ]**"
                    log.info(content)
            elif not resp['result']['isSignIn']:
                if not self.isReward():
                    if self.get_reward(resp['result']['signInDay']):
                        content = f"✅第{sgin_day}天已签到: 获得奖励：**[{reward_name}]**"
                        log.info(content)
                    else:
                        content = f"✅第{sgin_day}天已签到: 获得奖励：**[ 失败 ]**"
                        log.info(content)
                else:
                    content = f"🔁第{sgin_day}天已签到: 已获得奖励：**[{reward_name}]**"
                    log.info(content)     
        else:
            content = f"❌签到失败，请检查token是否正确"
            log.info(content)
            

        return content