<p align="center">
    <img src="https://www.clover1420.top/img/aa.jpg" width="auto" height="200">
</p>
<h1 align="center">自动签到</h1>
<p align="center">
    <img src="https://img.shields.io/badge/python-v3.10.4-blue" alt="python"/>
    <img src="https://img.shields.io/github/v/tag/clover1420/AutoSign?label=version" alt="version"/>
</p>
<p align="center">
    <a href="https://github.com/clover1420/AutoSign" style="text-decoration:none">
        <img src="https://img.shields.io/twitter/url?label=github&logo=github&style=social&url=https%3A%2F%2Fgithub.com%2Fclover1420%2FAutoSign" alt="GitHub"/>
    </a>
    <a href="https://gitee.com/clover1314/AutoSign" style="text-decoration:none">
        <img src="https://img.shields.io/twitter/url?label=gitee&logo=gitee&style=social&url=https%3A%2F%2Fgitee.com%2Fclover1314%2Fauto-sign" alt="GitHub"/>
    </a>
</p>
本项目用于需要手动每天签到的场景，使用本项目解放双手。本项目自动每天签到并推送到各社交应用上，目前支持qmsg，sever酱，企业微信，钉钉

<hr style="height: 1px;">
<h2 align="center">目前支持</h2>
<table align="center" border="1" style="text-align:center">
  <tr>
    <th style="text-align:center">应用</th>
    <th style="text-align:center">是否需要cookie</th>
    <th style="text-align:center">是否需要密码</th>
    <th style="text-align:center">是否可用</th>
    <th style="text-align:center">功能</th>
  </tr>
  <tr>
    <td><a href="https://miuiver.com/">MIUI历史版本</a></td>
    <td>❌</td>
    <td>✅</td>
    <td>✅</td>
    <td>每日签到得积分</td>
  </tr>
  <tr>
    <td><a href="https://www.3839.com/">好游快报</a></td>
    <td>✅</td>
    <td>❌</td>
    <td>✅</td>
    <td>每日爆米花浇水</td>
  </tr>
  <tr>
    <td><a href="https://www.xiaoheihe.cn/home">小黑盒</a></td>
    <td>✅</td>
    <td>❌</td>
    <td>✅</td>
    <td>每日签到得盒币</td>
  </tr>
  <tr>
    <td><a href="https://www.jiaoyimao.com/">交易猫</a></td>
    <td>✅</td>
    <td>❌</td>
    <td>✅</td>
    <td>每日签到得积分</td>
  </tr>
  <tr>
    <td><a href="https://cloud.189.cn/web/login.html">天翼云盘</a></td>
    <td>❌</td>
    <td>✅</td>
    <td>✅</td>
    <td>每日签到抽奖得空间</td>
  </tr>
  <tr>
    <td><a href="https://cg.163.com/#/mobile">网易云游戏</a></td>
    <td>✅</td>
    <td>❌</td>
    <td>✅</td>
    <td>每日签到获取使用时间和成长值</td>
  </tr>
</table>

<br>

---

**使用**：

1. 下载本项目

2. 解压本项目压缩包,在解压目录中**Shift+右键** 打开你的命令提示符cmd或powershell

3. 执行 `pip install -r requirements.txt` 安装模块

4. 打开目录中的**config.py**文件，填写cookie。

5. 运行**index.py**文件。

<br>

# 使用腾讯云函数运行

1. 打开并登录[云函数控制台](https://console.cloud.tencent.com/scf/list)。

2. 新建云函数 - 自定义创建，函数类型选`事件函数`，部署方式选`代码部署`，运行环境选 `Python3.6`.

3. 提交方法选`本地上传文件夹`，并在下方的函数代码处上传整个项目文件夹。

4. 执行方法填写 `index.main_handler`.

5. 展开高级配置，将执行超时时间修改为 `300 秒`，其他保持默认。

6. 展开触发器配置，选中自定义创建，触发周期选择`自定义触发周期`，并填写表达式`0 0 7 * * * *`（此处为每天上午 7 时运行一次，可以自行修改）

7. 完成

# 使用阿里云函数运行

1. 打开并登录[云函数控制台](https://fcnext.console.aliyun.com/overview)。

2. 函数及服务 - 创建服务(名称随便填，日志服务会收费可以关闭) - 创建函数(从零开始创建，函数名称随便填) - 运行环境选择python3.6及以上。

3. 代码上传方式选择`本地上传文件夹`并在下方的选择文件夹处上传整个项目文件夹。

4. 其余的默认就行

5. 配置触发器选择`定时触发器`，触发名称随便填，触发方式自定义，`cron表达式参照腾讯云函数表达式`

6. 创建完成到`函数配置`把`环境信息，超时时间改成300到600之间`

7. 完成

# cookie 获取

### 好游快爆

1. 用手机进行抓包复制请求体里面的的数据填入好游快爆的cookie
<p align="center">
    <img src="https://www.clover1420.top/img/a1.jpg!/format/webp/lossless/true" width="auto" height="200">
    <img src="https://www.clover1420.top/img/a2.jpg!/format/webp/lossless/true" width="auto" height="200">
</p>


### 小黑盒

1. 用手机进行抓包复制cookie的的数据填入小黑盒的cookie heybox_id，heybox_id可以在请求链接获取，imei请求连接里面获得 `注意imei可以不填，但有可能会封号`

### 交易猫

1. 用手机进行抓包复制cookie的的数据填入交易猫的cookie

### 网易云游戏

1. 首先我们进入[官网](https://cg.163.com/#/mobile)，进行登录。

2. 然后用F12打开开发者工具后使用Ctrl+F5进行刷新。

3. 找到@me这一项，然后在右边找到Authorization将冒号后面的内容复制下来就是我们所需要的Cookie。
