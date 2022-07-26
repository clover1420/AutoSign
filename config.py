# 推送配置
push = {
    # 推送方式
    # 支持qmsg酱 server酱 企业微信推送 钉钉机器人推送
    # qmsg,server,epwc,dingtalk
    # 为空或False则不进行推送
    "PushMode":"dingtalk",
    # 推送配置
    "PushKey":{
        # qmsg酱配置
        "Qmsg":"",
        # Server酱配置
        "Server":"",
        # 企业微信推送配置
        # 获取配置可以看 Server酱 的企业微信配置 https://sct.ftqq.com/forward
        "Epwc":{
            # 企业ID
            "EnterpriseId":"",
            # 应用ID/AgentId
            "AppId":"",
            # 应用Secret
            "AppSecret":"",
            # 推送UID
            "UserUid":""
        },
         # 钉钉机器人token获取 https://open.dingtalk.com/document/robots/custom-robot-access
         # 复制access_token=后面的token
        "Dingtalk":{
            # 机器人token
            "token":"",
            # 可选：创建机器人勾选“加签”选项时使用
            "secret":"",
            # 被@人的用户userid。选填
            "atuser":"",
            # 被@人的手机号。选填
            "atMobiles":"",
            # 是否@所有人。
            "isAtAll":False
        }
    }
}

#签到token
SignToken = {
    #好游快报 token
    "gtfed":{
        "switch":True,
        "cookie":""
    },
    #miui历史版本签到
    "MiUI":{
        "switch":True,
        # 用户账号
        "user":"",
        # 用户密码
        "password":""
    },
    # 小黑盒签到 heybox_id 必填
    "XiaoHeiHe":{
        "switch":True,
        "cookie":"",
        "imei":"",
        "heybox_id":""
    },
    # 交易猫
    "JiaoYiMao":{
        "switch":True,
        "cookie":""
    },
    # 天翼云盘 
    # 填入账号密码
    "tyyp":{
        "switch":True,
        # 账号
        "username":"",
        # 密码
        "password":""
    },
    # 网易云游戏
    "wyyyx":{
        "switch":False,
        "cookie":""
    }
}