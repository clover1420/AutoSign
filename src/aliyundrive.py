import requests
from src.log import Log


log = Log()

class Aliyundrive:
    def __init__(self, coofig):
        self.token = self.get_access_token(coofig['token'])

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
            token = self.token
            url = 'https://member.aliyundrive.com/v1/activity/sign_in_reward'
            headers = {
                "Content-Type": "application/json",
                "Authorization": token,
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 D/C501C6D2-FAF6-4DA8-B65B-7B8B392901EB"
            }
            body = {
                'signInDay': day
            }

            resp = requests.post(url, json=body, headers=headers).json()

            name = resp['result']['name']
            description = resp['result']['description']
            return {'name': name, 'description': description}
        except Exception as e:
            log.error(f"获取签到奖励异常={e}")

        return {'name': 'null', 'description': 'null'}
    

    # 签到
    def sign_in(self):
        url = "https://member.aliyundrive.com/v2/activity/sign_in_info"
        #url = 'https://member.aliyundrive.com/v2/activity/sign_in_list'
        #url = 'https://member.aliyundrive.com/v1/activity/sign_in_list'
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.token,
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 D/C501C6D2-FAF6-4DA8-B65B-7B8B392901EB"
        }
        body = {}

        resp = requests.post(url, json=body, headers=headers).json()
        return resp
    

    def sgin(self):
        Issgin = False

        # 签到
        resp = self.sign_in()

        if resp['success']:
            if not resp['result']['isSignIn']:
                reward = self.get_reward(resp['result']['signInDay'])
                if reward['name'] != 'null':
                    name = reward['name']
                    description = reward['description']
                else:
                    name = '无奖励'
                    description = ''
                #today_info = '✅' if i['day'] == result['signInCount'] else '☑'
                log.info(f"✅打卡第{resp['result']['day']}天，获得奖励：**[{name}#->{description}]**")
                log_info = f"✅打卡第{resp['result']['day']}天，获得奖励：**[{name}#->{description}]**"#->{description}]**"
            else:
                if not Issgin:
                    self.sgin()
                    Issgin = True
                log.info(f"❌未打卡，请手动打卡")
                log_info = f"❌打卡第{resp['result']['day']}天: 获得奖励：失败**"#->{description}]**"
                
        else:
            log.info(f"签到失败，请检查token是否正确")
            log_info = f"❌签到失败，请检查token是否正确"

        return log_info