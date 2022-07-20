from src.log import Log
from src.Push import Push
from config import push,SignToken
from src.Sign import gtfed,Miui,XiaoHeiHe,JiaoYiMao,TYYP,wyyyx
log = Log()

def run():
    data = "今日签到结果:"
    if SignToken['MiUI']['switch']:
        body = Miui(SignToken)
        data = data+"\n"+body.Sign()
    if SignToken['gtfed']['switch']:
        body = gtfed(SignToken)
        data = data+"\n"+body.Sign()
    if SignToken['XiaoHeiHe']['switch']:
        body = XiaoHeiHe(SignToken)
        data = data+"\n"+body.Sgin()
    if SignToken['JiaoYiMao']['switch']:
        body = JiaoYiMao(SignToken)
        data = data+"\n"+body.Sgin()
    if SignToken['tyyp']['switch']:
        body = TYYP(SignToken)
        data = data+"\n"+body.Sgin()
    if SignToken['wyyyx']['switch']:
        body = wyyyx(SignToken)
        data = data+"\n"+body.Sgin()
    ts = Push(data,push)
    ts.push()
    log.info("\n"+data)
    
