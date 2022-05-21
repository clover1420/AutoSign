from src.log import Log
from src.Push import Push
from config import push,SignToken
from src.Sign import gtfed,Miui

log = Log()

def run():
    data = ""
    if SignToken['MiUI']['switch']:
        aa = Miui(SignToken)
        data = data+aa.Sign()
    ts = Push(data,push)
    ts.push()