# Weather-Push

QQ、群推送今日天气（python+云函数）

github项目地址：https://github.com/xingjiahui/Weather-Push

# 介绍

## 功能介绍

- 支持推送到QQ、群，数目无限制
- 不同QQ、群可推送不同地区天气
- 推送内容丰富（日期，地区，天气，最高气温，最低气温，当前气温，风向，风力，空气指数，pm2.5指数，运动指数，天气小提示，能见度等内容）

## 运行界面

1. 执行日志：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/bbc3f72840f5c7ba845edb9beae38af2.png" width="70%"/>

2. QQ推送：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/55ed82d679b0bfa6fa588763a87e0c14.png" width="70%"/>
   
3. 群推送：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/3225d04005669f4812ffc8c0d0b961c9.png" width="70%"/>

   注意：为了降低接口压力和避免不必要问题，两次推送强制间隔20s+。

## 使用须知

1. 免费，腾讯云函数每月100万次免费调用额度，本项目每天只调用一次：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/e7d342f9854e007545d4f373e5debe79.png" width="70%"/>

2. 所有接收推送的QQ、群均需要添加机器人为好友（不然怎么给你推送）


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

   注意：尽管云函数有直接上传zip的选项，但我尝试了几次均上传失败，所以请务必解压后上传。

## 添加好友

1. qq扫描二维码，添加该机器人为好友：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/de589671f1a0cda2eff145a15324bad2.png" width="30%"/>

2. 群推送：添加好友后，将其拉入群聊（注意保护群聊隐私）。

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

   - 高级配置：

     <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/bf3ee3ec6efb2f04c0da3cb689dc221c.png" width="70%"/>

   - 其余配置项默认即可，点击完成

5. 按下图 `上传` 前面解压的文件夹，点击 `保存`：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/6329d7786535df00256c291008ef3965.png" width="70%"/>

6. 项目上传成功：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/c8ae64c9a9bfbc323b508d76fcd749cf.png" width="70%"/>

## 配置文件

1. 打开配置文件：左侧文件树中找到 `userData.yml` 文件，双击打开：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/acd985156af55ce53ede998a70e2550d.png" width="70%"/>

   注意：填写完成后，按下快捷键：`ctrl+s` 保存修改

2. 推送到QQ：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/ec1c9d12e466ebe0f34bc8fab285fbc0.png" width="70%"/>

3. 推送到QQ群：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/09/46bf7e087ec046614b37e8a82ca30e0a.png" width="70%"/>

   注意：要添加多个QQ、群时，按序号依次添加即可，注意缩进。

## 测试运行

1. 完成以上步骤，点击下图中的 `保存并测试`：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/8ca0413e26e52921687ed50881e8646e.png" width="70%"/>

2. 运行成功：

   - 执行日志：

     <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/bbc3f72840f5c7ba845edb9beae38af2.png" width="70%"/>

   - QQ、群推送：

     <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/cad8c973acc2df9ede4bf5e36f9310e7.png" width="40%"/>

   - 今日天气：

     <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/ada05801aa1fd3e53852ddb9d5abe482.png" width="70%"/>

# 脚本维护

## 定时触发

1. 创建触发器：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/10/17/440eab62174e21c346c9f2097261ec0f.png" width="70%"/>

2. 运行结果：

   <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/8ed89283594131b858a4c4fd205afa48.png" width="70%"/>

   注意：不要尝试与推送机器人对话，他不会回复你的

## 问题反馈

1. 项目 issues 地址：https://github.com/xingjiahui/Weather-Push/issues
2. 作者博客留言板：https://plushine.cn/messageboard/

## 更新日志

- `v2.0` 2020.11.10

  - 修复因云函数重复执行导致的重复推送问题

  - 修复因qmsg缓存异常导致的推送昨日天气的bugs

  - 弃用 `高德地图` api、`一言` api、`Qmsg酱` api

  - 简化配置，支持同时推送到QQ和群

  - 不同QQ、群可推送不同地区天气

  - 丰富推送内容（显示今日天气对应表情）

  - 项目快照：

    <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/55ed82d679b0bfa6fa588763a87e0c14.png" width="70%"/>

- `v1.0` 2020.10.17

  - 通过高德地图api获取天气信息

  - 支持多用户（多地区）天气推送

  - 推送内容添加 `一言` 短句

  - 脚本支持部署到云函数

  - 项目快照：

    <img src="https://cdn.jsdelivr.net/gh/xingjiahui/CDN@latest/2020/11/10/37933c73b83219eae0e887e61f88d2b0.png" width="70%"/>

## 声明

- 此脚本是作者利用业余时间所写，禁止用于商业、非法用途 
- 此脚本无任何恶意代码，但可能存在些许bug，因此所造成的损失与本人无关 
- 使用、运行本脚本即代表同意上述声明

# 感谢

1. 服务支持：
   - ~~[高德地图](https://lbs.amap.com/api/webservice/guide/api/weatherinfo/#t1)：提供免费天气API~~
   - [腾讯云函数](https://cloud.tencent.com/product/scf)：触发、执行python项目
   - ~~[Qmsg酱](https://qmsg.zendee.cn/)：QQ消息推送API~~
   
   - ~~[一言](https://api.uixsj.cn/hitokoto/index.html)：一言API~~
   - [QQPusher](http://qqpusher.yanxianjun.com/doc/)：QQ、QQ群消息推送API
   - [实况天气](https://tianqiapi.com/index/doc?version=v61)：天气APi
2. 技术支持：
   - [博客园-阿宅gogo](https://www.cnblogs.com/wbw-test/p/11580887.html)：python发送get请求
   - [CSDN-站在风口](https://blog.csdn.net/abby1559/article/details/79971957)：python字典初始化
   - [CSDN-占海](https://blog.csdn.net/chenzhanhai/article/details/106782325)：腾讯云函数添加依赖函数库
   - [CSDN-marselha](https://blog.csdn.net/marselha/article/details/91872832)：关于UnicodeDecodeError: 'gbk' codec can't decode byte 的解决方法
   - [CSDN-GhostRiderQin](https://blog.csdn.net/qq_40986486/article/details/103934408)：python加载YAML文件警告：YAMLLoadWarning: calling yaml.load() without... 的解决方法
   - [工具邦](http://cn.piliapp.com/emoji/list/weather/)：天气表情
