import requests
import time
import hmac
import hashlib
import base64
import urllib.parse
from src.log import Log

log = Log()

class Push():
    """
    msg : 消息内容
    push ： 推送的配置
    """
    def __init__(self,msg,push) -> None:
        self.PushMode = push['PushMode']
        self.qmsg_key = push['Qmsg']['key']
        self.Server_key = push['Server']['key']
        self.EnterpriseId = push['Epwc']['EnterpriseId']
        self.AppId = push['Epwc']['AppId']
        self.AppSecret = push['Epwc']['AppSecret']
        self.UserUid = push['Epwc']['UserUid']
        self.Dingtalk_token = push['Dingtalk']['token']
        self.Dingtalk_secret = push['Dingtalk']['secret']
        self.Dingtalk_atuser = push['Dingtalk']['atuser']
        self.Dingtalk_atMobiles = push['Dingtalk']['atMobiles']
        self.Dingtalk_isAtAll = push['Dingtalk']['isAtAll']
        self.wxhookurl = push['Wxhook']['url']
        self.msg = msg

    #qmsg酱推送
    def Qmsg(self) -> None:
        if self.qmsg_key == "":
            log.info("没有配置qmsg酱key")
        else:
            try:
                qmsg_url = f'https://qmsg.zendee.cn/send/{self.qmsg_key}'
                data = {'msg': self.msg}
                zz = requests.post(url=qmsg_url,data=data).json()
                if zz['code'] == 0:
                    log.info("qmsg酱"+zz['reason'])
                else:
                    log.info("qmsg酱"+zz['reason'])
            except Exception as e:
                log.error("qmsg酱可能挂了:"+e)

    #Sever酱推送
    def Server(self,title="米游社签到") -> None:
        if self.Server_key == "":
            log.info("没有Server酱cookie")
        else:
            Server_url = f"https://sctapi.ftqq.com/{self.Server_key}.send"
            data = {
                "title":title,
                "desp":self.msg
            }
            zz = requests.post(url=Server_url,data=data).json()
            if zz['code'] == 0:
                log.info("Server推送成功")
            else:
                log.info("Server推送失败"+zz['message'])
    
    # 企业微信推送
    def Epwc(self):
        try:
            if self.AppId != "" and self.AppSecret != "" and self.UserUid != "" and self.EnterpriseId != "":
                def GetToken():
                    url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.EnterpriseId}&corpsecret={self.AppSecret}&debug=1'
                    response = requests.get(url=url).json()
                    return response['access_token']
                url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={GetToken()}"
                body = {
                    "touser" : self.UserUid,
                    "msgtype" : "text",
                    "agentid" : int(self.AppId),
                    "text" : {"content" : self.msg},
                    "safe":0,
                    "duplicate_check_interval": 1800
                }
                response = requests.post(url=url,json=body).json()
                if response['errcode'] == 0:
                    log.info("企业微信推送成功")
                else:
                    log.info("企业微信推送失败")
            else:
                log.info("企业微信：配置没有填写完整")
        except Exception as e:
            log.info(f"企业微信推送时出现错误,错误码:{e}")

    #钉钉机器人推送
    def Dingtalk(self) -> None:
        def webhook():
            timestamp = str(round(time.time() * 1000))
            secret = self.Dingtalk_secret
            secret_enc = secret.encode('utf-8')
            string_to_sign = '{}\n{}'.format(timestamp, secret)
            string_to_sign_enc = string_to_sign.encode('utf-8')
            hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
            sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
            webhook = f'https://oapi.dingtalk.com/robot/send?access_token={self.Dingtalk_token}&timestamp={timestamp}&sign={sign}'
            # 返回请求链接
            return webhook

        # 消息体构建
        data = {
            "at": {
                "atMobiles":[self.Dingtalk_atMobiles],
                "atUserIds":[self.Dingtalk_atuser],
                "isAtAll": self.Dingtalk_isAtAll
            },
            "text": {
                "content":self.msg
                },
            "msgtype":"text"
        }
        
        if self.Dingtalk_token == "":
            log.info("没有配置钉钉机器人的Token")
        else:
            try:
                if self.Dingtalk_secret != "":
                    url = webhook()
                else:
                    url = f'https://oapi.dingtalk.com/robot/send?access_token={self.Dingtalk_token}'
                # 发送消息
                zz = requests.post(url=url,json=data).json()
                if zz['errcode'] == 0:
                    log.info("钉钉机器人推送成功")
                else:
                    log.info("钉钉机器人:"+zz['errmsg'])
            except Exception as e:
                log.error("钉钉机器人可能挂了:"+e)

    # 企业微信webhook推送
    def wxwebhook(self):
        head = {
            "Content-Type": "application/json"
        }
        data = {
            "msgtype": "text",
            "text": {
                "content": self.msg
            }
        }
        if self.wxhookurl != "":
            try:
                zz = requests.post(url=self.wxhookurl,headers=head,json=data).json()
                if zz['errcode'] == 0:
                    log.info("企业微信hook推送成功")
                else:
                    log.info(f"企业微信hook推送失败:{zz}")
            except Exception as e:
                log.error(f"企业微信hook推送出现错误:{e}")
        else:
            log.info("企业微信hook推送的url为空。")

        

        
    def push(self):
        if self.PushMode == "" or not self.PushMode:
            log.info("配置了不进行推送")
        elif self.PushMode == "Qmsg":
            self.Qmsg()
        elif self.PushMode == "Server":
            self.Server()
        elif self.PushMode == "Epwc":
            self.Epwc()
        elif self.PushMode == "Dingtalk":
            self.Dingtalk()
        elif self.PushMode == "Wxhook":
            self.wxwebhook()
        else:
            log.info("推送配置错误")
            
