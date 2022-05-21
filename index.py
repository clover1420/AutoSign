from main import run

# -------  腾讯云函数启动模块  --------#
def main_handler(event,context):
    run()


# -------  本地调试启动模块  --------#
if __name__ == '__main__':
    run()