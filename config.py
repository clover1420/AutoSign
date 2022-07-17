# 推送配置
push = {
    # 推送方式
    # 支持qmsg酱 server酱 企业微信推送
    # qmsg,server,epwc
    # 为空或False则不进行推送
    "PushMode":"epwc",
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
    # 小黑盒签到
    "XiaoHeiHe":{
        "switch":True,
        "cookie":"",
        "imei":""
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
    }
}