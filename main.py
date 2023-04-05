import time
from src.log import Log
from src.Push import Push
from steat import push,SignToken
from src.hykb import HaoYouKuaiBao
from src.Sign import Miui,XiaoHeiHe,JiaoYiMao,TYYP,wyyyx
log = Log()

def run():
    #开始时间
    Begin = time.time()
    #程序主体
    data = "今日签到结果:\n\n"
    if SignToken['MiUI']['switch']:
        body = Miui(SignToken)
        data += "MIUI历史版本:\n"+body.Sign()
    if SignToken['hykb']['switch']:
        body = HaoYouKuaiBao(SignToken)
        data += "\n\n好游快爆:\n"+ body.Sign()
    if SignToken['XiaoHeiHe']['switch']:
        body = XiaoHeiHe(SignToken)
        data += "\n\n小黑盒:\n"+body.Sgin()
    if SignToken['JiaoYiMao']['switch']:
        body = JiaoYiMao(SignToken)
        data += "\n\n交易猫:\n"+body.Sgin()
    if SignToken['tyyp']['switch']:
        body = TYYP(SignToken)
        data += "\n\n天翼云盘:\n"+body.Sgin()
    if SignToken['wyyyx']['switch']:
        body = wyyyx(SignToken)
        data += "\n\n网易云游戏:\n"+body.Sgin()
    # 结束时间
    end = time.time()
    sum = f"\n\n本次运行时间{round(end-Begin,3)}秒"
    data = data + "\n" + sum
    # 推送消息
    ts = Push(data,push)
    ts.push()

    log.info(sum)
    log.info("\n"+data)

if __name__ == '__main__':
    run()