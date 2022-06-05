# 推送配置
push = {
    # 推送方式
    # 支持qmsg酱 server酱 企业微信推送
    # qmsg,server,epwc
    # 为空或False则不进行推送
    "PushMode":"epwc",
    "PushKey":{
        # qmsg酱配置
        "Qmsg":"8f5ee9dc8f176a9b99aa0c941d37405e",
        # Server酱配置
        "Server":"SCT22994TyjZD1mmHwm754dbciNBEFXFB",
        # 企业微信推送配置
        # 获取配置可以看 Server酱 的企业微信配置 https://sct.ftqq.com/forward
        "Epwc":{
            # 企业ID
            "EnterpriseId":"ww5ab02ffa0a17526f",
            # 应用ID/AgentId
            "AppId":"1000002",
            # 应用Secret
            "AppSecret":"toAM06DW4L59X4rxJvLKJEk1AYGHWfqiZxN4kP_2eKQ",
            # 推送UID
            "UserUid":"SiYeCao"
        }
    }
}

#签到token
SignToken = {
    #好游快报 token
    "gtfed":{
        "switch":True,
        "cookie":"ac=Watering&r=0.1399304193190738&scookie=4%7C0%7C14155929%7C57mB5Y2OLeWmgumjjg%3D%3D%7Ckb70BC9668C52C9E846EF562AD5560D6DC%7CGvSioRVxpvbWpvXf7jejpJZnGJ9rpvZUGipfpR7UGJZ%3D%251%7C0cdaa46bdc4b84e8aaa2ac8e476406ba&device=kb70BC9668C52C9E846EF562AD5560D6DC"
    },
    #miui历史版本签到
    "MiUI":{
        "switch":True,
        # 用户账号
        "user":"748883120@qq.com",
        # 用户密码
        "password":"luojiba666"
    },
    # 小黑盒签到
    "XiaoHeiHe":{
        "switch":True,
        "cookie":"pkey=MTY0Mzg2MzE1MS4wXzE1MDgzNzExbnZoeHBneHlqdmtuc3ZmcA____;x_xhh_tokenid=BqCfFYwNxz7c42znG2hVGqULDL8+YcPZhQovD/JNVCQUTn74rEr8+ms4SFSaNM0D+26aTWTVoQv+rpgKnPzQuPw==",
        "imei":"3144140618ffa42a"
    },
    # 交易猫
    "JiaoYiMao":{
        "switch":True,
        "cookie":"service_ticket=;ssids=1620977152890833;_did=YH2ygxDifiEDAA6wMV75K10e;jym_utdid=YH2ygxDifiEDAA6wMV75K10e;ctoken=HT-x5YUi3IF7iyVDXY6FBc6g;cna=N9ZpGoULTSUCAXSpAyTEo/Xy;clientWidth=400;logTraceJymId=e85a51f49935-4311-8037-cc95;shopfc=2;track_id=spma_1652621552_01256668;actk=351d536ffcdd35a6749ab0d2db911596;ssts=9556be10969a52640bd4698fc07cd69a;actks=fbbaac23df675357f9d93445c1744d87;t_id=app1652955214960;Hm_lvt_47366dcc92e834539e7e9c3dcc2441de=1653481650;aplus_from=JYN_548;aplus_modelType=jym;sfroms=JYN_548;ieu_member_sid=jym001165050615332957237233019699771830046af07bcd5f7fdae7256feb250b7c03e;ieu_member_app_key=23072786;ieu_member_biz_id=jiaoyimao;_samesite_flag_=true;tfstk=cRldBFgo6_9dMy4tuvpizeMlGA-cZMj7qMZGwbLmAOIJJo1RiVGmgr49OPaTnFC..;l=eB_4UvAuLo6Ir2EOBOfwlurza77OSCOxiuPzaNbMiOCP_D1B5hmhW6fFq3Y6C3hRh68HR3lbtqHwBeYB4HKKnxv9XzSHbhkmn;Hm_lpvt_47366dcc92e834539e7e9c3dcc2441de=1653483899;isg=BAIC_WGX1FPBgsiPVdT2aW5BWApk0wbtCsKmgEwbL3Ugn6AZNGMU_NzWSt1F_36F;munb=2212595766427;_nk_=t-2212595766427-10000;cookie2=1e213a1f510c35ba3d990bcbc36dcc6d;csg=87ad015a;t=6e5a6575723545bd932959bcf86453a1;_tb_token_=fe7a94f87e553;jym_session_id=jym0011653483153329572372330198281349600b243e9aec9fd453b2cd19a7b6d6f859f;session=1653483620366285-4;EGG_SESS=PJoPzG5RvspeYQ-zEX1gB0qF0s1lJHSjGdb-QpoXxIZVqaGKF-jKFNnJXG2nMCwVzwZnqiyTPIxmQyoiMZVd4R8iJ0AYobEsQB3ojc3Ox75I3oGmv8vzdd3PrfNmLoe7LuUB5G723HXkzEDKD_TGxeHIhIh6RbhXr_2qnFLjJgM="
    },
    # 天翼云盘 
    # 填入账号密码
    "tyyp":{
        "switch":True,
        # 账号
        "username":"16683086171",
        # 密码
        "password":"Luojiba666@"
    }
}