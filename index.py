# -*- coding: utf8 -*-
import requests
import json
import yaml
import time


def getApi(name, url, params):
    '''
    get方式调用api
    :param name: api名称
    :param url: api链接
    :param params: api参数（dict）
    :return: api返回值
    '''
    res = json.loads(requests.get(url, params).text)
    print('【{}】接口测试正常✔'.format(name))
    return res


def getWeather(dirItem):
    '''
    调用api获取天气信息
    :param dirId: 地区编码
    :return: 今日天气信息
    '''
    weatherUrl = "https://v0.yiketianqi.com/api"
    weatherParams = {'key': 'c369a5115a88fe279e8c6de3ba5fd8c7',
                     'extensions': 'all',
                     'version': 'v61',
                     'appid': '37964223',
                     'appsecret': '1mnzfhBP',
                     'province': dirItem[0],
                     'city': dirItem[1],
                     }
    return getApi('天气api', weatherUrl, weatherParams)


# def getYiyan():
#     '''
#     一言
#     :return: 一言
#     '''
#     yiyanUrl = 'https://api.uixsj.cn/hitokoto/get'
#     yiyanParams = {'type': 'hitokoto', 'code': 'json'}
#     return '【一言】' + str(getApi('一言', yiyanUrl, yiyanParams)['content']) + "\n"


def getInfo(res):
    '''
    从获取的天气信息中筛选要发送的数据
    :param res: 天气信息
    :return: 要发送的数据
    '''
    dataList = []
    date = res['date']
    week = res['week']
    wea = res['wea']
    wea_img = res['wea_img']
    tem = res['tem']
    tem1 = res['tem1']
    tem2 = res['tem2']
    win = res['win']
    win_speed = res['win_speed']
    visibility = res['visibility']
    air_level = res['air_level']
    air_tips = res['air_tips']
    pm25_desc = res['aqi']['pm25_desc']
    yundong = res['aqi']['yundong']

    dataList.extend(
        [date, week, wea, wea_img, tem, tem1, tem2, win, win_speed, visibility, air_level, air_tips, pm25_desc,
         yundong])  # python同时添加多个元素
    return dataList


def QQPusher(qqNum, dataList):
    '''
    调用QQPusher接口，给指定qq发送消息
    :param qqNum: qq
    :param dataList: 要发送的数据列表
    :param Token: 调用QQPusher所需的Token
    '''
    QQPusherUrl = 'http://api.qqpusher.yanxianjun.com/send_private_msg'
    QQPusherParams = {
        'token': 'ec74aea16af00cff8cf883d800bfc954',
        'user_id': qqNum,
        'message': '今日天气推送🍀 \n---\n{}，{}\n{} ， {}\n{}  {}，{}/{} ℃\n{}，{}\n空气质量：{}，pm2.5：{}\n运动指数：{}\n---\n{}\n---\n当前气温：{}℃，能见度：{}\n温馨提示：疫情期间，外出请佩戴口罩！'.format(
            dataList[0], dataList[1], dataList[14], dataList[15], dataList[2], dataList[16], dataList[6], dataList[5],
            dataList[7], dataList[8], dataList[10], dataList[12], dataList[13], dataList[11], dataList[4], dataList[9])
    }
    return getApi('QQPusher', QQPusherUrl, QQPusherParams)


def QQGroupPusher(qqNum, dataList):
    '''
    调用QQPusher接口，给指定qq群发送消息
    :param qqNum: qq群
    :param dataList: 要发送的数据列表
    :param Token: 调用QQPusher所需的Token
    '''
    QQPusherUrl = 'http://api.qqpusher.yanxianjun.com/send_group_msg'
    QQPusherParams = {
        'token': 'ec74aea16af00cff8cf883d800bfc954',
        'group_id': qqNum,
        'message': '今日天气推送 🍀 \n---\n{}，{}\n{} ， {}\n{}  {}，{}/{} ℃\n{}，{}\n空气质量：{}，pm2.5：{}\n运动指数：{}\n---\n{}\n---\n当前气温：{}℃，能见度：{}\n温馨提示：疫情期间，外出请佩戴口罩！'.format(
            dataList[0], dataList[1], dataList[14], dataList[15], dataList[2], dataList[16], dataList[6], dataList[5],
            dataList[7], dataList[8], dataList[10], dataList[12], dataList[13], dataList[11], dataList[4], dataList[9])
    }
    return getApi('QQPusher', QQPusherUrl, QQPusherParams)


def main_handler(event, context):
    file = open('userData.yml', 'r', encoding="utf-8")  # 从配置文件中获取数据（str）
    file_data = file.read()
    file.close()

    data = yaml.load(file_data, Loader=yaml.FullLoader)  # str转dict

    userData = data['userData']

    dataDict = []  # 存放用户数据（地区，qq）
    for key, value in userData.items():
        dict = {'province': value[0], 'city': value[1], 'qq': str(value[2])}
        dataDict.append(dict)

    for i in range(len(dataDict)):
        print("---正在获取【{},{}】的天气！---".format(dataDict[i]['province'], dataDict[i]['city']))
        res = getWeather((dataDict[i]['province'], dataDict[i]['city']))  # 获取天气信息

        dataList = getInfo(res)  # 存放从api中获取的天气天气数据
        dataList.append(dataDict[i]['province'])
        dataList.append(dataDict[i]['city'])
        dataList.append(
            dataList[3].replace('xue', '❄').replace('lei', '⚡').replace('shachen', '🌪').replace('wu', '🌫').replace(
                'bingbao', '🌨').replace('yun', '☁').replace('yu', '🌧').replace('yin', '🌥').replace('qing', '☀'))
        time.sleep(2)

        # dataList.append(getYiyan())  # 一言
        # time.sleep(2)

        if 'g' in dataDict[i]['qq']:
            dataDict[i]['qq'] = dataDict[i]['qq'][1:]
            QQGroupPusher(dataDict[i]['qq'], dataList)
        else:
            QQPusher(dataDict[i]['qq'], dataList)
        print("---天气推送成功！---")
        time.sleep(20)
