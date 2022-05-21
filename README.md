# AutoSign

#### 介绍
![](https://img.shields.io/badge/python-v3.10.4-blue) 

自动签到各种应用脚本

[github仓库](https://github.com/clover1420/AutoSign)

[gitee仓库](https://gitee.com/clover1314/auto-sign)

目前支持 <a href="https://miuiver.com/"><font color=#FF4500>MIUI历史版本</font></a>

# 使用
1. 下载本项目

2. 解压本项目压缩包,在解压目录中**Shift+右键** 打开你的命令提示符cmd或powershell

3. 执行 `pip install -r requirements.txt` 安装模块

4. 打开目录中的**config.py**文件，填写cookie。

5. 运行**index.py**文件。

# 使用腾讯云函数运行

1. 打开并登录[云函数控制台](https://console.cloud.tencent.com/scf/list)。

2. 新建云函数 - 自定义创建，函数类型选`事件函数`，部署方式选`代码部署`，运行环境选 `Python3.6`.

3. 提交方法选`本地上传文件夹`，并在下方的函数代码处上传整个项目文件夹。

4. 执行方法填写 `index.main_handler`.

5. 展开高级配置，将执行超时时间修改为 `300 秒`，其他保持默认。

6. 展开触发器配置，选中自定义创建，触发周期选择`自定义触发周期`，并填写表达式`0 0 7 * * * *`（此处为每天上午 7 时运行一次，可以自行修改）

7. 完成

# cookie 获取
MIUI 历史版本只需要账号,密码，不需要cookie  