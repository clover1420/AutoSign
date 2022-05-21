import requests
from src.log import Log
log = Log()

class Push():
    """
    msg : 消息内容
    push ： 推送的配置
    """
    def __init__(self,msg,push) -> None:
        self.qmsg_key = push['PushKey']['Qmsg']
        self.Server_key = push['PushKey']['Server']
        self.PushMode = push['PushMode']
        self.msg = msg

    #qmsg酱推送
    def Qmsg(self) -> None:
        if self.qmsg_key == "":
            log.info("没有配置qmsg酱key")
        else:
            try:
                qmsg_url = f'https://qmsg.zendee.cn/send/{self.qmsg_key}'
                data = {'msg': "米游社原神签到\n"+self.msg}
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
            if zz['code'] == "0":
                log.info("Server推送成功")
            else:
                log.info("Server推送失败"+zz['message'])

    def push(self):
        if self.PushMode == "qmsg":
            self.Qmsg()
        elif self.PushMode == "server":
            self.Server()

