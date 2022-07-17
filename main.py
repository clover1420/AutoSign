from src.log import Log
from src.Push import Push
from config import push,SignToken
from src.Sign import gtfed,Miui,XiaoHeiHe,JiaoYiMao,TYYP
log = Log()

def run():
    data = "今日签到结果:"
    if SignToken['MiUI']['switch']:
        miui = Miui(SignToken)
        data = data+"\n"+miui.Sign()
    if SignToken['gtfed']['switch']:
        gtfeds = gtfed(SignToken)
        data = data+"\n"+gtfeds.Sign()
    if SignToken['XiaoHeiHe']['switch']:
        xiaoheihe = XiaoHeiHe(SignToken)
        data = data+"\n"+xiaoheihe.Sgin()
    if SignToken['JiaoYiMao']['switch']:
        aa = JiaoYiMao(SignToken)
        data = data+"\n"+aa.Sgin()
    if SignToken['tyyp']['switch']:
        aa = TYYP(SignToken)
        data = data+"\n"+aa.Sgin()
    ts = Push(data,push)
    ts.push()
    log.info("\n"+data)
    
