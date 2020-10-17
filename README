# Weather-Push

QQ推送今日天气（python+云函数）

github项目地址：https://github.com/xingjiahui/Weather-Push

# 介绍

## 运行界面

1. 执行日志：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/7ffc20db4830f8554849cb6c01951084.png" width="70%"/>

2. QQ推送：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/00a48936d897a9d7d6a9af0c61b8e86c.png" width="50%"/>

## 使用须知

1. 免费，腾讯云函数每月100万次免费调用额度，本项目每天只调用一次：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/e7d342f9854e007545d4f373e5debe79.png" width="70%"/>

2. 所有获取推送消息的QQ均需要添加QQ机器人为好友（不然怎么给你推送）

3. QQ机器人可能会出现消息重复推送的问题（机器人接口问题，等待作者修复）

## 语言库

- python 3.8
- requests 2.24.0（接口get请求）
- pyyaml 5.3.1（配置文件）
- json 2.0.9（数据格式化）

# 使用该项目

## 下载项目

1. 进入 [Weather-Push](https://github.com/xingjiahui/Weather-Push) 项目主页，按下图依次点击 `code` 、`Download ZIP`：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/d88653d8849d9841b92b51b98f4ecca4.png" width="70%"/>

2. 解压缩到桌面：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/8dbab4406941f24cfca997c2ff99d339.png" width="70%"/>

   注意：尽管云函数有直接上传zip的选项，但我尝试了几次均上传失败，所以务必要进行此步骤

## 获取QmsgKey

1. 进入 [Qmsg官网](https://qmsg.zendee.cn/) 登录获取接口地址（QmsgKey）
2. 接口获取教程：https://plushine.cn/34430.html#%E6%8F%90%E9%86%92%E5%8A%9F%E8%83%BD

3. 注意：

   - 选择qmsg酱时一定要选择 `消息推送服务`：

     <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/691326bf67604d5c4c59d4fc2637883d.png" width="70%"/>

   - 添加要推送天气的QQ：

     <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/39ab26b2d16c3b4675b02cfb9481ff87.png" width="70%"/>

     注意：作者暂未开放推送消息到QQ群

## 创建云函数

1. 进入 [腾讯云函数](https://console.cloud.tencent.com/scf/index?rid=4) 首页：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/f3178eb44e1264a27c02e41e9a51b51e.png" width="70%"/>

   注意：若账号注册有问题，请自行百度

2. 点击左侧 `函数服务` ，`新建` 云函数：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/48d34dd37daf27b823f50107b556f37c.png" width="70%"/>

3. 填写 `基本信息`：

   - 函数名称：自定义
   - 运行环境：python 3.6
   - 其余均为默认，点击 `下一步`

4. 填写 `函数配置`：

   - 描述：QQ推送今日天气（python+云函数）
   - 其余均为默认，点击 `完成`

5. 按下图 `上传` 前面解压的文件夹，点击 `保存`：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/6329d7786535df00256c291008ef3965.png" width="70%"/>

6. 项目上传成功：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/c8ae64c9a9bfbc323b508d76fcd749cf.png" width="70%"/>

## 配置文件

1. 查找所在城市dirId：

   - 左侧文件树中找到 `dirId.csv` 文件，双击打开：

     <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/a2d11d5b017ae37898bc3130359f01a2.png" width="70%"/>

   - 快捷键： `ctrl+f` ，输入城市名（烟台为例）按下回车，复制后面对应的dirId：

     <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/f7672cf458df5aa4c5fea0e11ed2eb59.png" width="70%"/>

2. 填写配置文件：

   - 左侧文件树中找到 `userData.yml` 文件，双击打开：

     <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/2e6541b5d1aa08901483b0207bc3b69e.png" width="70%"/>

   - 按照下图填写配置：

     <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/b87e1c139300a17352553212bffe39e9.png" width="70%"/>

     注意：填写完成后，按下快捷键：`ctrl+s` 保存修改

3. 可不可以同时给多个用户发送多地天气呢？可以的，按照下图添加城市信息就可以实现啦！

   - qmsg官网添加要推送的QQ：

     <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/39ab26b2d16c3b4675b02cfb9481ff87.png" width="70%"/>

     注意：记得添加机器人为好友才能收到消息呀！

   - 按照下图格式在 `userData.yml` 中添加城市信息：

     <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/175a092e6ba66dec0f99c487bb9974b7.png" width="70%"/>

     注意：严格按照上图格式添加新城市信息

## 测试运行

1. 完成以上步骤，点击下图中的 `保存并测试`：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/8ca0413e26e52921687ed50881e8646e.png" width="70%"/>

2. 运行成功：

   - 执行日志：

     <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/a786d736e02c56133d5d6bd67cd349c3.png" width="70%"/>

   - QQ推送：

     <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/e98e6e481920ae31efb0ce59e7881911.png" width="30%"/>

   - 今日天气：

     <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/00a3d31838073bc2158cbc39ebfd068c.png" width="50%"/>

# 脚本维护

## 定时触发

1. 按照下图操作：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/440eab62174e21c346c9f2097261ec0f.png" width="90%"/>

2. 运行结果：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/3c127ca0e99818054724ab1edde11150.png" width="50%"/>

   注意：不要尝试与推送机器人对话，他不会回复你的

## 问题反馈

1. 项目 issues 地址：https://github.com/xingjiahui/Weather-Push/issues
2. 作者博客留言板：https://plushine.cn/messageboard/

# 感谢

1. 服务支持：
   - [高德地图](https://lbs.amap.com/api/webservice/guide/api/weatherinfo/#t1)：提供免费天气API
   - [腾讯云函数](https://cloud.tencent.com/product/scf)：触发、执行python项目
   - [Qmsg酱](https://qmsg.zendee.cn/)：QQ消息推送API
   - [一言](https://api.uixsj.cn/hitokoto/index.html)：一言API
2. 技术支持：
   - [博客园-阿宅gogo](https://www.cnblogs.com/wbw-test/p/11580887.html)：python发送get请求
   - [CSDN-站在风口](https://blog.csdn.net/abby1559/article/details/79971957)：python字典初始化
   - [CSDN-占海](https://blog.csdn.net/chenzhanhai/article/details/106782325)：腾讯云函数添加依赖函数库
   - [CSDN-marselha](https://blog.csdn.net/marselha/article/details/91872832)：关于UnicodeDecodeError: 'gbk' codec can't decode byte 的解决方法
   - [CSDN-GhostRiderQin](https://blog.csdn.net/qq_40986486/article/details/103934408)：python加载YAML文件警告：YAMLLoadWarning: calling yaml.load() without... 的解决方法
