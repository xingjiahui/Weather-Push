# -*- coding: utf8 -*-
import requests
import json
import yaml


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


def getWeather(dirId):
    '''
    调用api获取天气信息
    :param dirId: 地区编码
    :return: 今日天气信息
    '''
    weatherUrl = "https://restapi.amap.com/v3/weather/weatherInfo"
    weatherParams = {'key': 'c369a5115a88fe279e8c6de3ba5fd8c7', 'city': dirId, 'extensions': 'all'}
    return getApi('天气', weatherUrl, weatherParams)


def getWarn(weather):
    '''
    根据天气情况，返回提示语句
    :param weather: 天气情况
    :return: 提示语句
    '''
    warn = ''
    if '雨' in weather:
        warn = '今天可能有雨，注意保暖，出门带伞！\n'
    elif '晴' in weather:
        warn = '好天气，好心情!\n'
    return warn


def getYiyan():
    '''
    一言
    :return: 一言
    '''
    yiyanUrl = 'https://api.uixsj.cn/hitokoto/get'
    yiyanParams = {'type': 'hitokoto', 'code': 'json'}
    return '【一言】' + str(getApi('一言', yiyanUrl, yiyanParams)['content']) + "\n"


def getInfo(res):
    '''
    从获取的天气信息中筛选要发送的数据
    :param res: 天气信息
    :return: 要发送的数据
    '''
    dataList = []
    form = res['forecasts'][0]
    city = form['city']
    time = form['casts'][0]['date']
    week = form['casts'][0]['week']
    weather = form['casts'][0]['dayweather']
    dataList.extend([city, time, week, weather])  # python同时添加多个元素
    return dataList


def qmsgPush(qqNum, dataList, qmsgKey):
    '''
    调用qmsg接口，给指定qq发送消息
    :param qqNum: qq
    :param dataList: 要发送的数据列表
    :param qmsgKey: 调用qmsg接口所需的key
    '''
    qmsgUrl = 'https://qmsg.zendee.cn:443/send/{}'.format(qmsgKey)
    qmsgParams = {
        'msg': '今日天气🍀\n---\n{}，周{}\n{}天气：{}\n{}---\n{}'.format(dataList[1], dataList[2], dataList[0], dataList[3],
                                                                dataList[4], dataList[5]),
        'qq': qqNum}
    return getApi('qmsg', qmsgUrl, qmsgParams)


# def main_handler(event, context):
if __name__ == '__main__':
    file = open('userData.yml', 'r', encoding="utf-8")
    file_data = file.read()
    file.close()

    data = yaml.load(file_data, Loader=yaml.FullLoader)

    qmsgKey = data['qmsgKey']

    userData = data['userData']

    dataDict = []
    for key, value in userData.items():
        dict = {}
        dict['dirName'] = value[0]
        dict['dirId'] = value[1]
        dict['qq'] = value[2]
        dataDict.append(dict)

    for i in range(len(dataDict)):
        print("---正在获取【{}】今日天气！---".format(dataDict[i]['dirName']))
        res = getWeather(dataDict[i]['dirId'])  # 获取天气信息

        dataList = getInfo(res)  # 返回列表存放要发送的天气信息
        dataList.append(getWarn(dataList[3]))  # 根据天气判断是否要添加“带伞提示”,并将数据添加到列表中
        dataList.append(getYiyan())  # 一言

        qmsgPush(dataDict[i]['qq'], dataList, qmsgKey)
        print("---天气推送成功！---")
