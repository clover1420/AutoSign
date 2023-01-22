import requests
import src.setting as url
from src.log import Log
from urllib.parse import urlencode,parse_qs

log = Log()


class HaoYouKuaiBao():
    """好游快爆签到
    """
    Url = 'https://huodong3.3839.com/n/hykb/grow/ajax.php'
    SowUrl = ""
    def __init__(self,SignToken) -> None:
        self.gtfed = SignToken['hykb']['cookie']
        self.head = {
            "User-Agent":"Mozilla/5.0 (Linux; Android 7.0; Meizu S6 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.110 Mobile Safari/537.36Androidkb/1.5.5.305(android;Meizu S6;7.0;720x1374;4G);@4399_sykb_android_activity@",
            "Origin":"https://huodong3.3839.com",
            "X-Requested-With":"XMLHttpRequest",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Referer":"https://huodong3.3839.com/n/hykb/grow/index.php",
	    }
        
    def Sign(self):
        if self.gtfed != "":
            zz = requests.post(url=self.Url,data=self.gtfed,headers=self.head).json()
            if zz['key'] == 'ok':
                if zz['csd_jdt'] == "100%":
                    cookie = self.gtfed.replace("Watering","PlantRipe")
                    SowRes = requests.post(url=self.Url,data=cookie,headers=self.head).json()
                    if SowRes['key'] == 513:
                        cookie = self.gtfed.replace("Watering","PlantSow")
                        SowRes = requests.post(url=self.Url,data=cookie,headers=self.head).json()
                        if SowRes['key'] == "ok":
                            log.info("好游快爆:收获，重新播种完成")
                            return "收获，重新播种完成"
                        else:
                            log.info("好游快爆:收获完成，重新播种失败")
                            return "收获完成，重新播种失败"
                    else:
                        log.info("好游快爆:收获，重新播种完成")
                        return "收获，重新播种完成"
                else:
                    log.info("好游快爆:浇水完成")
                    return "浇水完成"
            elif  zz['key'] == '502':
                cookie = self.gtfed.replace("Watering","PlantRipe")
                SowRes = requests.post(url=self.Url,data=cookie,headers=self.head).json()
                if SowRes['key'] == 513:
                    cookie = self.gtfed.replace("Watering","PlantSow")
                    SowRes = requests.post(url=self.Url,data=cookie,headers=self.head).json()
                    if SowRes['key'] == "ok":
                        log.info("好游快爆:收获，重新播种完成")
                        return "收获，重新播种完成"
                    else:
                        log.info("好游快爆:收获，重新播种完成")
                        return "收获，重新播种完成"
                else:
                    log.info("好游快爆:收获失败，请手动收获")
                    return "收获失败，请手动收获"
            elif zz['key'] == '501':
                cookie = self.gtfed.replace("Watering","PlantSow")
                SowRes = requests.post(url=self.Url,data=cookie,headers=self.head).json()
                if SowRes['key'] == "ok":
                    log.info("好游快爆:收获，重新播种完成")
                    return "收获，重新播种完成"
                else:
                    log.info("好游快爆:收获完成，重新播种失败")
                    return "收获完成，重新播种失败"
            else:
                log.info(f"好游快爆:{zz['info']}")
                return zz['info']
        else:
            log.info("好游快爆:没有配置cookie")
            return "没有配置cookie"
           