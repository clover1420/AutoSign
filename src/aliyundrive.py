import requests
from src.log import Log


log = Log()

class Aliyundrive:
    def __init__(self, coofig):
        self.token = self.get_access_token(coofig['token'])
        pass

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

            resp = requests.post(url, json=data_dict, headers=headers)
            resp_json = resp.json()

            #log.info(f"resp_json={resp_json}")

            token = {}
            token['access_token'] = resp_json.get('access_token', "")
            token['refresh_token'] = resp_json.get('refresh_token', "")
            token['expire_time'] = resp_json.get('expire_time', "")
            access_token = token['access_token']
        except Exception as e:
            log.error(f"获取异常:{e}")

        return access_token
    
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

            resp = requests.post(url, json=body, headers=headers)

            resp_json = resp.json()
            result = resp_json.get('result', {})
            name = result.get('name', '')
            description = result.get('description', '')
            return {'name': name, 'description': description}
        except Exception as e:
            log.error(f"获取签到奖励异常={e}")

        return {'name': 'null', 'description': 'null'}
    

    def sgin(self):

        url = 'https://member.aliyundrive.com/v1/activity/sign_in_list'
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.token,
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 D/C501C6D2-FAF6-4DA8-B65B-7B8B392901EB"
        }
        body = {}

        resp = requests.post(url, json=body, headers=headers).json()

        if resp['code'] == "AccessTokenInvalid":
                log.info(f"请检查token是否正确")
        elif resp['code'] is None:
            result = resp['result']
            if len(result['signInLogs']) > 0:
                for i in result['signInLogs']:
                    if i['status'] == "":
                        log.info("签到信息获取异常")
                    elif i['status'] == "miss":
                        pass
                        #log.warning(f"第{i['day']}天未打卡")
                    elif i['status'] == "normal":
                        if not i['isReward']:
                            reward = self.get_reward(i['day'])
                        else:
                            reward = i['reward']
                        if reward:
                            name = reward['name']
                            description = reward['description']
                        else:
                            name = '无奖励'
                            description = ''
                        today_info = '✅' if i['day'] == result['signInCount'] else '☑'
                        log_info = f"{today_info}打卡第{i['day']}天，获得奖励：**[{name}->{description}]**"
        return log_info
