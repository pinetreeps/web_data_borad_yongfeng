# _*_ coding:utf-8 _*_
# Filename: check_info.py
# Author: pang song
# python 3.6
# Date: 2018/12/26
'''
三、信息接口
'''
import random
import logging
from utils import mysql_utils

logger = logging.getLogger("main")

WEEK_NAMES = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']


def get_name_by_id(check_id):
    '''
    get name by check_id
    :return: name
    '''
    check_name = ''
    data_conn = mysql_utils.Database()
    sql1 = "select position_name from yf_bim_position_info where position_id = '{pid}'".format(pid=check_id)
    row1 = data_conn.query_one(sql1)
    logger.debug(row1)
    if row1 != None:
        check_name = row1[0]
    return check_name

def get_device_name_by_id(check_id):
    '''
    get name by check_id
    :return: name
    '''
    check_name = ''
    data_conn = mysql_utils.Database()
    sql1 = "select device_name, device_code, device_type, device_position_id from yf_bim_device_info where device_id = '{did}'".format(did=check_id)
    row1 = data_conn.query_one(sql1)
    logger.debug(row1)
    if row1 != None:
        check_name = row1[0]
    return check_name


# --------------1、项目概况模块 ------------------

def get_area_overview():
    '''
    查询园区概况
    :return: dict
    '''
    '''
    园区概况
    占地面积	29450
    建筑数量	8
    总建筑面积	58900
    容积率	2.0
    绿地率	30
    入驻企业统计	345
    园区人员统计	4589
    招商企业分析	239
    '''
    # # 测试数据
    test_data_area_overview = {
        "land_area": "29450",
        "buildings_amount": "1",
        "buildings_area": "7643",
        "floor_area_ratio": "2.0",
        "greening_rate": "30",
        "company_amount": "1",
        "area_people_amount": "300",
        "companys_ratio": [
            {
                "ratio_name": "事业单位",
                "ratio_value": "1"
            },
            {
                "ratio_name": "其他单位",
                "ratio_value": "0"
            }]
    }
    return test_data_area_overview


def get_building_overview():
    '''
    查询建筑概况
    :return: dict
    '''
    '''
    建筑概况
    建筑名称	永丰B5综合服务楼
    使用功能	综合服务楼
    建筑面积	7643m²
    建筑高度	25m
    建筑时间	2018
    建筑层数	5
    '''
    # # 测试数据
    test_data_building_overview = {
        "building_name":"西北旺镇中午服务中心",
        "building_function":"综合服务楼",
        "building_area":"7643",
        "building_time":"2018",
        "building_height":"25",
        "building_floors":"5"
    }
    return test_data_building_overview


def get_env_outdoor():
    '''
    查询室外环境 实时
    :return: dict
    '''
    # # 测试数据
    test_data_env_outdoor = {
        "temperature":"7",
        "humidity":"31",
        "wind_direction":"南",
        "wind_speed":"1.2",
        "precipitation":"0",
        "air_pressure":"102.3",
        "pm2.5":"120"
    }
    return test_data_env_outdoor

def env_outdoor_history(data_type):
    '''
        查询室外环境 历史数据
        :return: dict
        '''
    # # 测试数据
    test_data_env_outdoor_history = { "data_list":[]}
    if 'year' == data_type:
        test_data_env_outdoor_history["data_list"] = [
            {"data_time": "1", "temperature_high":"5", "temperature_low":"-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
            {"data_time": "2", "temperature_high":"8", "temperature_low":"-8", "humidity": "40", "wind_speed": "2.2", "precipitation": "20", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "3", "temperature_high":"13", "temperature_low":"0", "humidity": "40", "wind_speed": "0.5", "precipitation": "60", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "4", "temperature_high":"20", "temperature_low":"1", "humidity": "40", "wind_speed": "0.8", "precipitation": "50", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "5", "temperature_high":"26", "temperature_low":"16", "humidity": "40", "wind_speed": "0.7", "precipitation": "50", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "6", "temperature_high":"28", "temperature_low":"18", "humidity": "40", "wind_speed": "0.9", "precipitation": "100", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "7", "temperature_high":"30", "temperature_low":"22", "humidity": "40", "wind_speed": "0.5", "precipitation": "200", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "8", "temperature_high":"35", "temperature_low":"22", "humidity": "40", "wind_speed": "0.6", "precipitation": "180", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "9", "temperature_high":"34", "temperature_low":"18", "humidity": "40", "wind_speed": "0.9", "precipitation": "80", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "10", "temperature_high":"26", "temperature_low":"16", "humidity": "40", "wind_speed": "1.3", "precipitation": "20", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "11", "temperature_high":"16", "temperature_low":"8", "humidity": "40", "wind_speed": "2.1", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "500"},
            {"data_time": "12", "temperature_high":"7", "temperature_low":"-6", "humidity": "40", "wind_speed": "1.2", "precipitation": "0", "air_pressure": "102.3",   "pm2.5": "420"},
            ]
    elif 'month' == data_type:
        for i in range(1, 31):
            row_data = {
                "data_time": str(i),
                "temperature_high": str(random.randint(1, 10)),
                "temperature_low": str(random.randint(-10, 3)),
                "humidity": str(random.randint(10, 35)),
                "wind_speed": str(random.randint(0, 3)) + '.' + str(random.randint(0, 10)),
                "precipitation": str(random.randint(0, 200)),
                "air_pressure": str(random.randint(100, 105)),
                "pm2.5": str(random.randint(80, 500))
            }
            test_data_env_outdoor_history["data_list"].append(row_data)

    elif 'day' == data_type:
        # 模拟数据
        temperature_high_list = [-3,-3,-2,-1,-1,0,0,1,4,6,7,10,11,11,12,11,10,9,8,5,4,3,2,1]
        for i in range(0, 24):
            row_data = {
                "data_time": str(i),
                "temperature_high": str(temperature_high_list[i]),
                "temperature_low": str(temperature_high_list[i] - random.randint(0, 4)),
                "humidity": str(random.randint(10, 35)),
                "wind_speed": str(random.randint(0, 3)) + '.' + str(random.randint(0, 10)),
                "precipitation": str(random.randint(0, 200)),
                "air_pressure": str(random.randint(100, 105)),
                "pm2.5": str(random.randint(80, 500))
            }
            test_data_env_outdoor_history["data_list"].append(row_data)
    return test_data_env_outdoor_history

def get_env_indoor(position_id):
    '''
    查询室内环境 实时
    :return: dict
    '''
    position_name = get_name_by_id(position_id)

    # # 测试数据
    test_data = {
        "position_name":"{}".format(position_name),
        "temperature": str(random.randint(22, 24)),
        "humidity": str(random.randint(30, 40)),
        "voc": '0.0'+ str(random.randint(0, 9)),
        "pm2.5": str(random.randint(5, 15))
    }
    return test_data


def env_indoor_history(position_id, data_type):
    '''
    查询室内环境 历史数据
    :return: dict
    '''
    # # 测试数据
    position_name = get_name_by_id(position_id)
    test_data_env_indoor_history = {
        "position_name": "{}".format(position_name),
        "data_list": []
    }
    if 'year' == data_type:
        test_data_env_indoor_history["data_list"] = [
            {"data_time": "1", "temperature_high":"5", "temperature_low":"-10", "humidity": "10", "voc":"0.1", "pm2.5": "15"},
            {"data_time": "2", "temperature_high":"8", "temperature_low":"-8", "humidity": "14",  "voc":"0.05", "pm2.5": "15"},
            {"data_time": "3", "temperature_high":"13", "temperature_low":"0", "humidity": "15",  "voc":"0.08", "pm2.5": "10"},
            {"data_time": "4", "temperature_high":"20", "temperature_low":"1", "humidity": "21",  "voc":"0.05", "pm2.5": "5"},
            {"data_time": "5", "temperature_high":"26", "temperature_low":"16", "humidity": "30", "voc":"0.09", "pm2.5": "12"},
            {"data_time": "6", "temperature_high":"28", "temperature_low":"18", "humidity": "34", "voc":"0.07", "pm2.5": "12"},
            {"data_time": "7", "temperature_high":"30", "temperature_low":"22", "humidity": "45", "voc":"0.08", "pm2.5": "13"},
            {"data_time": "8", "temperature_high":"35", "temperature_low":"22", "humidity": "35", "voc":"0.05", "pm2.5": "5"},
            {"data_time": "9", "temperature_high":"34", "temperature_low":"18", "humidity": "41", "voc":"0.06", "pm2.5": "8"},
            {"data_time": "10", "temperature_high":"26", "temperature_low":"16", "humidity": "22", "voc":"0.07", "pm2.5": "11"},
            {"data_time": "11", "temperature_high":"16", "temperature_low":"8", "humidity": "19", "voc":"0.06", "pm2.5": "14"},
            {"data_time": "12", "temperature_high":"7", "temperature_low":"-6", "humidity": "20", "voc":"0.02", "pm2.5": "6"},
            ]
    elif 'month' == data_type:
        for i in range(1, 31):
            row_data = {
                "data_time": str(i),
                "temperature_high": str(random.randint(16, 24)),
                "temperature_low": str(random.randint(16, 24)),
                "humidity": str(random.randint(25, 35)),
                "voc": '0.0'+ str(random.randint(0, 9)),
                "pm2.5": str(random.randint(5, 15))
            }
            test_data_env_indoor_history["data_list"].append(row_data)

    elif 'day' == data_type:
        for i in range(0, 24):
            row_data = {
                "data_time": str(i),
                "temperature_high": str(random.randint(16, 24)),
                "temperature_low": str(random.randint(16, 24)),
                "humidity": str(random.randint(25, 35)),
                "voc": '0.0'+ str(random.randint(0, 9)),
                "pm2.5": str(random.randint(5, 15))
            }
            test_data_env_indoor_history["data_list"].append(row_data)
    return test_data_env_indoor_history

def get_energy_overview(check_id):
    '''
    查询用能概况
    :return: dict
    '''
    check_name = get_name_by_id(check_id)
    # # 测试数据
    energy_overview_data = {
        "check_name":"{}".format(check_name),
        "electricity":[],
        "gas":[],
        "water":[]}

    for i in range(7):
        # 用电
        row_data1 = {
                "time": WEEK_NAMES[i],
                "value_list": [{"name":"照明","value": str(random.randint(1000, 1500))},
                               {"name":"空调", "value":"0",},
                               {"name":"插座","value": str(random.randint(200, 400))},
                               {"name":"厨房","value":"0",},
                               {"name":"其他","value":"0",},],
            }
        energy_overview_data["electricity"].append(row_data1)
        # 用气
        row_data2 = {
                        "time": WEEK_NAMES[i],
                        "value_list":[{"name":"采暖","value":"0",},{"name":"厨房", "value":"0",},{"name":"其他","value":"0",}]
                    }
        energy_overview_data["gas"].append(row_data2)
        # 用水
        row_data3 = {
                        "time": WEEK_NAMES[i],
                        "value_list": [{"name": "生活", "value": "0", }, {"name": "空调", "value": "0", },
                                       {"name": "厨房", "value": "0", }, {"name": "其他", "value": "0", }, ]
                    }
        energy_overview_data["water"].append(row_data3)

    test_data = {
        "check_name":"{}".format(check_name),
        "electricity":[
            {
                "time":"周一",
                "value_list": [{"name":"建筑","value":"231",},
                               {"name":"空调", "value":"3523",},
                               {"name":"电器","value":"2223",},
                               {"name":"其他","value":"1123",},],
            },
            {
                "time": "周二",
                "value_list": [{"name": "建筑", "value": "231", }, {"name": "空调", "value": "3523", },
                               {"name": "电器", "value": "2223", }, {"name": "其他", "value": "1123", }, ],
            },
            {
                "time": "周三",
                "value_list": [{"name": "建筑", "value": "231", }, {"name": "空调", "value": "3523", },
                               {"name": "电器", "value": "2223", }, {"name": "其他", "value": "1123", }, ],
            },
            {
                "time": "周四",
                "value_list": [{"name": "建筑", "value": "231", }, {"name": "空调", "value": "3523", },
                               {"name": "电器", "value": "2223", }, {"name": "其他", "value": "1123", }, ],
            },
            {
                "time": "周五",
                "value_list": [{"name": "建筑", "value": "231", }, {"name": "空调", "value": "3523", },
                               {"name": "电器", "value": "2223", }, {"name": "其他", "value": "1123", }, ],
            },
            {
                "time": "周六",
                "value_list": [{"name": "建筑", "value": "31", }, {"name": "空调", "value": "33", },
                               {"name": "电器", "value": "2223", }, {"name": "其他", "value": "3", }, ],
            },
            {
                "time": "周日",
                "value_list": [{"name": "建筑", "value": "10", }, {"name": "空调", "value": "23", },
                               {"name": "电器", "value": "20", }, {"name": "其他", "value": "23", }, ],
            },

        ],
        "gas":[
            {
                "time":"周一",
                "value_list":[{"name":"采暖","value":"0",},{"name":"厨房", "value":"0",},{"name":"其他","value":"0",},],
            },
            {
                "time": "周二",
                "value_list": [{"name":"采暖","value":"0",},{"name":"厨房", "value":"0",},{"name":"其他","value":"0",},],
            },
            {
                "time": "周三",
                "value_list": [{"name":"采暖","value":"0",},{"name":"厨房", "value":"0",},{"name":"其他","value":"0",},],
            },
            {
                "time": "周四",
                "value_list": [{"name":"采暖","value":"0",},{"name":"厨房", "value":"0",},{"name":"其他","value":"0",},],
            },
            {
                "time": "周五",
                "value_list": [{"name":"采暖","value":"0",},{"name":"厨房", "value":"0",},{"name":"其他","value":"0",},],
            },
            {
                "time": "周六",
                "value_list": [{"name":"采暖","value":"0",},{"name":"厨房", "value":"3",},{"name":"其他","value":"0",},],
            },
            {
                "time": "周日",
                "value_list": [{"name":"采暖","value":"0",},{"name":"厨房", "value":"0",},{"name":"其他","value":"0",},],
            },

        ],
        "water":[
            {
                "time":"周一",
                "value_list":[{"name":"生活","value":"0",},{"name":"空调", "value":"0",},{"name":"厨房","value":"0",},{"name":"其他","value":"0",},],
            },
            {
                "time": "周二",
                "value_list": [{"name": "生活", "value": "0", }, {"name": "空调", "value": "0", },
                               {"name": "厨房", "value": "0", }, {"name": "其他", "value": "0", }, ],
            },
            {
                "time": "周三",
                "value_list": [{"name": "生活", "value": "0", }, {"name": "空调", "value": "0", },
                               {"name": "厨房", "value": "0", }, {"name": "其他", "value": "0", }, ],
            },
            {
                "time": "周四",
                "value_list": [{"name": "生活", "value": "0", }, {"name": "空调", "value": "0", },
                               {"name": "厨房", "value": "0", }, {"name": "其他", "value": "0", }, ],
            },
            {
                "time": "周五",
                "value_list": [{"name": "生活", "value": "0", }, {"name": "空调", "value": "0", },
                               {"name": "厨房", "value": "0", }, {"name": "其他", "value": "0", }, ],
            },
            {
                "time": "周六",
                "value_list": [{"name": "生活", "value": "0", }, {"name": "空调", "value": "0", },
                               {"name": "厨房", "value": "0", }, {"name": "其他", "value": "0", }, ],
            },
            {
                "time": "周日",
                "value_list": [{"name": "生活", "value": "0", }, {"name": "空调", "value": "0", },
                               {"name": "厨房", "value": "0", }, {"name": "其他", "value": "0", }, ],
            },

        ],
    }
    # return test_data
    return energy_overview_data


def get_energy_electricity_overview(check_id):
    '''
    用电情况通用查询接口1，使用唯一id进行查询，园区用电、建筑用电返回各建筑、各层用电占比
    :return: dict
    '''
    check_name = get_name_by_id(check_id)
    # # 测试数据
    energy_electricity_overview_data = {
        "check_name":"{}".format(check_name),
        "electricity":str(random.randint(1200, 1900)),
        "history_year_list":[],
        "history_month_list": [],
        "history_day_list":[
            {"history_time": "1", "history_value": "126"},
            {"history_time": "2", "history_value": "96"},
            {"history_time": "3", "history_value": "76"},
            {"history_time": "4", "history_value": "66"},
            {"history_time": "5", "history_value": "87"},
            {"history_time": "6", "history_value": "81"},
            {"history_time": "7", "history_value": "92"},
            {"history_time": "8", "history_value": "126"},
            {"history_time": "9", "history_value": "286"},
            {"history_time": "10", "history_value": "326"},
            {"history_time": "11", "history_value": "456"},
            {"history_time": "12", "history_value": "526"},
            {"history_time": "13", "history_value": "326"},
            {"history_time": "14", "history_value": "561"},
            {"history_time": "15", "history_value": "526"},
            {"history_time": "16", "history_value": "626"},
            {"history_time": "17", "history_value": "621"},
            {"history_time": "18", "history_value": "426"},
            {"history_time": "19", "history_value": "536"},
            {"history_time": "20", "history_value": "426"},
            {"history_time": "21", "history_value": "526"},
            {"history_time": "22", "history_value": "226"},
            {"history_time": "23", "history_value": "126"},
            {"history_time": "0", "history_value": "26"},
        ],
        "electricity_ratio1": [
            {"ratio_id": "floor01", "ratio_name": "1层", "ratio_value": "115"},
            {"ratio_id": "floor02", "ratio_name": "2层", "ratio_value": "85"},
            {"ratio_id": "floor03", "ratio_name": "3层", "ratio_value": "95"},
            {"ratio_id": "floor04", "ratio_name": "4层", "ratio_value": "75"},
            {"ratio_id": "floor05", "ratio_name": "5层", "ratio_value": "56"},
        ],
        "electricity_ratio2": [
            {"ratio_id": "b01", "ratio_name": "照明", "ratio_value": "2345"},
            {"ratio_id": "b02", "ratio_name": "空调", "ratio_value": "0"},
            {"ratio_id": "b03", "ratio_name": "电器", "ratio_value": "545"},
            {"ratio_id": "b03", "ratio_name": "其他", "ratio_value": "0"},
        ]
    }
    for i in range(1, 13):
        row_data = {"history_time": str(i), "history_value":str(random.randint(1200, 1900)) }
        energy_electricity_overview_data["history_year_list"].append(row_data)

    for i in range(1, 31):
        row_data = {"history_time": str(i), "history_value":str(random.randint(1200, 1900)) }
        energy_electricity_overview_data["history_month_list"].append(row_data)


    test_data = {
        "check_name":"{}".format(check_name),
        "electricity":"178",
        "history_year_list":[
            {"history_time": "1", "history_value":"326" },
            {"history_time": "2", "history_value":"226" },
            {"history_time": "3", "history_value":"76" },
            {"history_time": "4", "history_value":"126" },
            {"history_time": "5", "history_value":"326" },
            {"history_time": "6", "history_value":"426" },
            {"history_time": "7", "history_value":"626" },
            {"history_time": "8", "history_value":"596" },
            {"history_time": "9", "history_value":"86" },
            {"history_time":"10", "history_value":"126" },
            {"history_time":"11", "history_value":"156" },
            {"history_time":"12", "history_value":"526" },
        ],
        "history_month_list":[
            {"history_time": "1", "history_value": "326"},
            {"history_time": "2", "history_value": "226"},
            {"history_time": "3", "history_value": "376"},
            {"history_time": "4", "history_value": "526"},
            {"history_time": "5", "history_value": "326"},
            {"history_time": "6", "history_value": "426"},
            {"history_time": "7", "history_value": "626"},
            {"history_time": "8", "history_value": "596"},
            {"history_time": "9", "history_value": "86"},
            {"history_time": "10", "history_value": "226"},
            {"history_time": "11", "history_value": "456"},
            {"history_time": "12", "history_value": "326"},
            {"history_time": "13", "history_value": "326"},
            {"history_time": "14", "history_value": "426"},
            {"history_time": "15", "history_value": "563"},
            {"history_time": "16", "history_value": "626"},
            {"history_time": "17", "history_value": "526"},
            {"history_time": "18", "history_value": "526"},
            {"history_time": "19", "history_value": "526"},
            {"history_time": "20", "history_value": "326"},
            {"history_time": "21", "history_value": "426"},
            {"history_time": "22", "history_value": "156"},
            {"history_time": "23", "history_value": "526"},
            {"history_time": "24", "history_value": "526"},
            {"history_time": "25", "history_value": "526"},
            {"history_time": "26", "history_value": "526"},
            {"history_time": "27", "history_value": "526"},
            {"history_time": "28", "history_value": "526"},
            {"history_time": "29", "history_value": "526"},
            {"history_time": "30", "history_value": "526"},
        ],
        "history_day_list":[
            {"history_time": "1", "history_value": "326"},
            {"history_time": "2", "history_value": "226"},
            {"history_time": "3", "history_value": "76"},
            {"history_time": "4", "history_value": "126"},
            {"history_time": "5", "history_value": "326"},
            {"history_time": "6", "history_value": "426"},
            {"history_time": "7", "history_value": "626"},
            {"history_time": "8", "history_value": "596"},
            {"history_time": "9", "history_value": "86"},
            {"history_time": "10", "history_value": "126"},
            {"history_time": "11", "history_value": "156"},
            {"history_time": "12", "history_value": "526"},
            {"history_time": "13", "history_value": "526"},
            {"history_time": "14", "history_value": "526"},
            {"history_time": "15", "history_value": "526"},
            {"history_time": "16", "history_value": "526"},
            {"history_time": "17", "history_value": "526"},
            {"history_time": "18", "history_value": "426"},
            {"history_time": "19", "history_value": "436"},
            {"history_time": "20", "history_value": "526"},
            {"history_time": "21", "history_value": "226"},
            {"history_time": "22", "history_value": "126"},
            {"history_time": "23", "history_value": "226"},
            {"history_time": "0", "history_value": "26"},
        ],
        "electricity_ratio1":[
            {"ratio_id":"floor01", "ratio_name":"1层", "ratio_value":"115"},
            {"ratio_id":"floor02", "ratio_name":"2层", "ratio_value":"85"},
            {"ratio_id":"floor03", "ratio_name":"3层", "ratio_value":"95"},
            {"ratio_id":"floor04", "ratio_name":"4层", "ratio_value":"75"},
            {"ratio_id":"floor05", "ratio_name":"5层", "ratio_value":"56"},
        ],
        "electricity_ratio2": [
            {"ratio_id": "b01","ratio_name": "照明","ratio_value": "2345"},
            {"ratio_id": "b02","ratio_name": "空调","ratio_value": "0"},
            {"ratio_id": "b03","ratio_name": "电器","ratio_value": "545"},
            {"ratio_id": "b03","ratio_name": "其他","ratio_value": "0"},
        ]
    }
    # return test_data
    return energy_electricity_overview_data


def get_energy_electricity(check_id):
    '''
    用电情况通用查询接口2，使用唯一id 查询设备用电（空调、电器）
    :return: dict
    '''
    check_name = get_name_by_id(check_id)
    # # 测试数据
    energy_electricity_data = {
        "check_name": "{}".format(check_name),
        "electricity": str(random.randint(100, 200)),
        "history_year_list": [],
        "history_month_list": [],
        "history_day_list":[
            {"history_time": "1", "history_value": "1"},
            {"history_time": "2", "history_value": "2"},
            {"history_time": "3", "history_value": "3"},
            {"history_time": "4", "history_value": "2"},
            {"history_time": "5", "history_value": "1"},
            {"history_time": "6", "history_value": "3"},
            {"history_time": "7", "history_value": "4"},
            {"history_time": "8", "history_value": "8"},
            {"history_time": "9", "history_value": "9"},
            {"history_time": "10", "history_value": "11"},
            {"history_time": "11", "history_value": "12"},
            {"history_time": "12", "history_value": "13"},
            {"history_time": "13", "history_value": "12"},
            {"history_time": "14", "history_value": "13"},
            {"history_time": "15", "history_value": "8"},
            {"history_time": "16", "history_value": "6"},
            {"history_time": "17", "history_value": "11"},
            {"history_time": "18", "history_value": "12"},
            {"history_time": "19", "history_value": "5"},
            {"history_time": "20", "history_value": "6"},
            {"history_time": "21", "history_value": "8"},
            {"history_time": "22", "history_value": "2"},
            {"history_time": "23", "history_value": "2"},
            {"history_time": "0", "history_value": "1"},
        ]
    }
    for i in range(1, 13):
        row_data = {"history_time": str(i), "history_value":str(random.randint(200, 300)) }
        energy_electricity_data["history_year_list"].append(row_data)

    for i in range(1, 31):
        row_data = {"history_time": str(i), "history_value":str(random.randint(100, 200)) }
        energy_electricity_data["history_month_list"].append(row_data)


    test_data = {
        "check_name":"{}".format(check_name),
        "electricity":"178",
        "history_year_list":[
            {"history_time": "1", "history_value":"326" },
            {"history_time": "2", "history_value":"226" },
            {"history_time": "3", "history_value":"76" },
            {"history_time": "4", "history_value":"126" },
            {"history_time": "5", "history_value":"326" },
            {"history_time": "6", "history_value":"426" },
            {"history_time": "7", "history_value":"626" },
            {"history_time": "8", "history_value":"596" },
            {"history_time": "9", "history_value":"86" },
            {"history_time":"10", "history_value":"126" },
            {"history_time":"11", "history_value":"156" },
            {"history_time":"12", "history_value":"526" },
        ],
        "history_month_list":[
            {"history_time": "1", "history_value": "326"},
            {"history_time": "2", "history_value": "226"},
            {"history_time": "3", "history_value": "76"},
            {"history_time": "4", "history_value": "126"},
            {"history_time": "5", "history_value": "326"},
            {"history_time": "6", "history_value": "426"},
            {"history_time": "7", "history_value": "626"},
            {"history_time": "8", "history_value": "596"},
            {"history_time": "9", "history_value": "86"},
            {"history_time": "10", "history_value": "126"},
            {"history_time": "11", "history_value": "156"},
            {"history_time": "12", "history_value": "526"},
            {"history_time": "13", "history_value": "526"},
            {"history_time": "14", "history_value": "526"},
            {"history_time": "15", "history_value": "526"},
            {"history_time": "16", "history_value": "526"},
            {"history_time": "17", "history_value": "526"},
            {"history_time": "18", "history_value": "526"},
            {"history_time": "19", "history_value": "526"},
            {"history_time": "20", "history_value": "326"},
            {"history_time": "21", "history_value": "426"},
            {"history_time": "22", "history_value": "526"},
            {"history_time": "23", "history_value": "526"},
            {"history_time": "24", "history_value": "526"},
            {"history_time": "25", "history_value": "526"},
            {"history_time": "26", "history_value": "526"},
            {"history_time": "27", "history_value": "526"},
            {"history_time": "28", "history_value": "526"},
            {"history_time": "29", "history_value": "526"},
            {"history_time": "30", "history_value": "526"},
        ],
        "history_day_list":[
            {"history_time": "1", "history_value": "326"},
            {"history_time": "2", "history_value": "226"},
            {"history_time": "3", "history_value": "76"},
            {"history_time": "4", "history_value": "126"},
            {"history_time": "5", "history_value": "326"},
            {"history_time": "6", "history_value": "426"},
            {"history_time": "7", "history_value": "626"},
            {"history_time": "8", "history_value": "596"},
            {"history_time": "9", "history_value": "86"},
            {"history_time": "10", "history_value": "126"},
            {"history_time": "11", "history_value": "156"},
            {"history_time": "12", "history_value": "526"},
            {"history_time": "13", "history_value": "526"},
            {"history_time": "14", "history_value": "526"},
            {"history_time": "15", "history_value": "526"},
            {"history_time": "16", "history_value": "526"},
            {"history_time": "17", "history_value": "526"},
            {"history_time": "18", "history_value": "426"},
            {"history_time": "19", "history_value": "436"},
            {"history_time": "20", "history_value": "526"},
            {"history_time": "21", "history_value": "226"},
            {"history_time": "22", "history_value": "126"},
            {"history_time": "23", "history_value": "226"},
            {"history_time": "0", "history_value": "26"},
        ]
    }
    # return test_data
    return energy_electricity_data

def get_energy_gas(check_id):
    '''
    查询用气情况
    :return: dict
    '''
    check_name = get_name_by_id(check_id)

    # # 测试数据
    energy_gas_data = {
        "check_name":"{}".format(check_name),
        "ac_gas": {
            "class_name": "采暖用气",
            "history_year_list":[],
            "history_month_list":[],
            "history_day_list":[]
        },
        "kitchen_gas": {
            "class_name": "厨房用气",
            "history_year_list": [],
            "history_month_list": [],
            "history_day_list": []
        }
    }
    for i in range(1, 13):
        row_data = {"history_time": str(i), "history_value":"0" }
        energy_gas_data["ac_gas"]["history_year_list"].append(row_data)
        energy_gas_data["kitchen_gas"]["history_year_list"].append(row_data)
    for i in range(1, 31):
        row_data = {"history_time": str(i), "history_value": "0"}
        energy_gas_data["ac_gas"]["history_month_list"].append(row_data)
        energy_gas_data["kitchen_gas"]["history_month_list"].append(row_data)
    for i in range(0, 24):
        row_data = {"history_time": str(i), "history_value": "0"}
        energy_gas_data["ac_gas"]["history_day_list"].append(row_data)
        energy_gas_data["kitchen_gas"]["history_day_list"].append(row_data)

    test_data = {
        "check_name":"{}".format(check_name),
        "ac_gas": {
            "class_name": "采暖用气",
            "history_year_list":[
                {"history_time": "1", "history_value":"326" },
                {"history_time": "2", "history_value":"226" },
                {"history_time": "3", "history_value":"76" },
                {"history_time": "4", "history_value":"126" },
                {"history_time": "5", "history_value":"326" },
                {"history_time": "6", "history_value":"426" },
                {"history_time": "7", "history_value":"626" },
                {"history_time": "8", "history_value":"596" },
                {"history_time": "9", "history_value":"86" },
                {"history_time":"10", "history_value":"126" },
                {"history_time":"11", "history_value":"156" },
                {"history_time":"12", "history_value":"526" },
            ],
            "history_month_list":[
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "526"},
                {"history_time": "19", "history_value": "526"},
                {"history_time": "20", "history_value": "326"},
                {"history_time": "21", "history_value": "426"},
                {"history_time": "22", "history_value": "526"},
                {"history_time": "23", "history_value": "526"},
                {"history_time": "24", "history_value": "526"},
                {"history_time": "25", "history_value": "526"},
                {"history_time": "26", "history_value": "526"},
                {"history_time": "27", "history_value": "526"},
                {"history_time": "28", "history_value": "526"},
                {"history_time": "29", "history_value": "526"},
                {"history_time": "30", "history_value": "526"},
            ],
            "history_day_list":[
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "426"},
                {"history_time": "19", "history_value": "436"},
                {"history_time": "20", "history_value": "526"},
                {"history_time": "21", "history_value": "226"},
                {"history_time": "22", "history_value": "126"},
                {"history_time": "23", "history_value": "226"},
                {"history_time": "0", "history_value": "26"},
            ]
        },
        "kitchen_gas": {
            "class_name": "厨房用气",
            "history_year_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
            ],
            "history_month_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "526"},
                {"history_time": "19", "history_value": "526"},
                {"history_time": "20", "history_value": "326"},
                {"history_time": "21", "history_value": "426"},
                {"history_time": "22", "history_value": "526"},
                {"history_time": "23", "history_value": "526"},
                {"history_time": "24", "history_value": "526"},
                {"history_time": "25", "history_value": "526"},
                {"history_time": "26", "history_value": "526"},
                {"history_time": "27", "history_value": "526"},
                {"history_time": "28", "history_value": "526"},
                {"history_time": "29", "history_value": "526"},
                {"history_time": "30", "history_value": "526"},
            ],
            "history_day_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "426"},
                {"history_time": "19", "history_value": "436"},
                {"history_time": "20", "history_value": "526"},
                {"history_time": "21", "history_value": "226"},
                {"history_time": "22", "history_value": "126"},
                {"history_time": "23", "history_value": "226"},
                {"history_time": "0", "history_value": "26"},
            ]
        }
    }
    # return test_data
    return energy_gas_data

def get_energy_water_overview(check_id):
    '''
    查询用水情况
    :return: dict
    '''
    check_name = get_name_by_id(check_id)

    # # 测试数据
    energy_water_overview_data = {
        "check_name":"{} 用水总览".format(check_name),
        "live_water": {
            "class_name": "生活用水",
            "history_year_list":[],
            "history_month_list":[],
            "history_day_list":[],
            "ratio_list":[
                {"ratio_id":"floor01", "ratio_name":"1层", "ratio_value":"0"},
                {"ratio_id":"floor02", "ratio_name":"2层", "ratio_value":"0"},
                {"ratio_id":"floor03", "ratio_name":"3层", "ratio_value":"0"},
                {"ratio_id":"floor04", "ratio_name":"4层", "ratio_value":"0"},
                {"ratio_id":"floor05", "ratio_name":"5层", "ratio_value":"0"},
            ]
        },
        "kitchen_water": {
            "class_name": "厨房用水",
            "history_year_list": [],
            "history_month_list": [],
            "history_day_list": [],
            "ratio_list": [
                {"ratio_id": "floor01", "ratio_name": "1号厨房", "ratio_value": "0"},
                {"ratio_id": "floor02", "ratio_name": "2号厨房", "ratio_value": "0"},
            ]
        },
        "ac_water": {
            "class_name": "空调用水",
            "history_year_list": [],
            "history_month_list": [],
            "history_day_list": []
        }
    }
    for i in range(1, 13):
        row_data = {"history_time": str(i), "history_value":"0" }
        energy_water_overview_data["live_water"]["history_year_list"].append(row_data)
        energy_water_overview_data["kitchen_water"]["history_year_list"].append(row_data)
        energy_water_overview_data["ac_water"]["history_year_list"].append(row_data)
    for i in range(1, 31):
        row_data = {"history_time": str(i), "history_value": "0"}
        energy_water_overview_data["live_water"]["history_month_list"].append(row_data)
        energy_water_overview_data["kitchen_water"]["history_month_list"].append(row_data)
        energy_water_overview_data["ac_water"]["history_month_list"].append(row_data)
    for i in range(0, 24):
        row_data = {"history_time": str(i), "history_value": "0"}
        energy_water_overview_data["live_water"]["history_day_list"].append(row_data)
        energy_water_overview_data["kitchen_water"]["history_day_list"].append(row_data)
        energy_water_overview_data["ac_water"]["history_day_list"].append(row_data)


    test_data = {
        "check_name":"{} 用水总览".format(check_name),
        "live_water": {
            "class_name": "生活用水",
            "history_year_list":[
                {"history_time": "1", "history_value":"326" },
                {"history_time": "2", "history_value":"226" },
                {"history_time": "3", "history_value":"76" },
                {"history_time": "4", "history_value":"126" },
                {"history_time": "5", "history_value":"326" },
                {"history_time": "6", "history_value":"426" },
                {"history_time": "7", "history_value":"626" },
                {"history_time": "8", "history_value":"596" },
                {"history_time": "9", "history_value":"86" },
                {"history_time":"10", "history_value":"126" },
                {"history_time":"11", "history_value":"156" },
                {"history_time":"12", "history_value":"526" },
            ],
            "history_month_list":[
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "526"},
                {"history_time": "19", "history_value": "526"},
                {"history_time": "20", "history_value": "326"},
                {"history_time": "21", "history_value": "426"},
                {"history_time": "22", "history_value": "526"},
                {"history_time": "23", "history_value": "526"},
                {"history_time": "24", "history_value": "526"},
                {"history_time": "25", "history_value": "526"},
                {"history_time": "26", "history_value": "526"},
                {"history_time": "27", "history_value": "526"},
                {"history_time": "28", "history_value": "526"},
                {"history_time": "29", "history_value": "526"},
                {"history_time": "30", "history_value": "526"},
            ],
            "history_day_list":[
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "426"},
                {"history_time": "19", "history_value": "436"},
                {"history_time": "20", "history_value": "526"},
                {"history_time": "21", "history_value": "226"},
                {"history_time": "22", "history_value": "126"},
                {"history_time": "23", "history_value": "226"},
                {"history_time": "0", "history_value": "26"},
            ],
            "ratio_list":[
                {"ratio_id":"floor01", "ratio_name":"1号楼*层01房间", "ratio_value":"45"},
                {"ratio_id":"floor02", "ratio_name":"1号楼*层02房间", "ratio_value":"85"},
                {"ratio_id":"floor03", "ratio_name":"1号楼*层03房间", "ratio_value":"95"},
                {"ratio_id":"floor04", "ratio_name":"1号楼*层04房间", "ratio_value":"25"},
                {"ratio_id":"floor05", "ratio_name":"1号楼*层05房间", "ratio_value":"15"},
            ]
        },
        "kitchen_water": {
            "class_name": "厨房用水",
            "history_year_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
            ],
            "history_month_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "526"},
                {"history_time": "19", "history_value": "526"},
                {"history_time": "20", "history_value": "326"},
                {"history_time": "21", "history_value": "426"},
                {"history_time": "22", "history_value": "526"},
                {"history_time": "23", "history_value": "526"},
                {"history_time": "24", "history_value": "526"},
                {"history_time": "25", "history_value": "526"},
                {"history_time": "26", "history_value": "526"},
                {"history_time": "27", "history_value": "526"},
                {"history_time": "28", "history_value": "526"},
                {"history_time": "29", "history_value": "526"},
                {"history_time": "30", "history_value": "526"},
            ],
            "history_day_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "426"},
                {"history_time": "19", "history_value": "436"},
                {"history_time": "20", "history_value": "526"},
                {"history_time": "21", "history_value": "226"},
                {"history_time": "22", "history_value": "126"},
                {"history_time": "23", "history_value": "226"},
                {"history_time": "0", "history_value": "26"},
            ],
            "ratio_list": [
                {"ratio_id": "floor01", "ratio_name": "1号厨房", "ratio_value": "45"},
                {"ratio_id": "floor02", "ratio_name": "2号厨房", "ratio_value": "85"},
            ]
        },
        "ac_water": {
            "class_name": "空调用水",
            "history_year_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
            ],
            "history_month_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "526"},
                {"history_time": "19", "history_value": "526"},
                {"history_time": "20", "history_value": "326"},
                {"history_time": "21", "history_value": "426"},
                {"history_time": "22", "history_value": "526"},
                {"history_time": "23", "history_value": "526"},
                {"history_time": "24", "history_value": "526"},
                {"history_time": "25", "history_value": "526"},
                {"history_time": "26", "history_value": "526"},
                {"history_time": "27", "history_value": "526"},
                {"history_time": "28", "history_value": "526"},
                {"history_time": "29", "history_value": "526"},
                {"history_time": "30", "history_value": "526"},
            ],
            "history_day_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "426"},
                {"history_time": "19", "history_value": "436"},
                {"history_time": "20", "history_value": "526"},
                {"history_time": "21", "history_value": "226"},
                {"history_time": "22", "history_value": "126"},
                {"history_time": "23", "history_value": "226"},
                {"history_time": "0", "history_value": "26"},
            ]
        }
    }
    # return test_data
    return energy_water_overview_data

def get_energy_check_hot(check_id):
    '''
    用电情况通用查询接口2，使用唯一id 查询设备用电（空调、电器）
    :return: dict
    '''
    check_name = get_name_by_id(check_id)

    energy_check_hot_data = {
        "check_name": "设备用热 {}".format(check_name),
        "hot": "178",
        "history_year_list": [],
        "history_month_list": [],
        "history_day_list": []
    }
    for i in range(1, 13):
        row_data = {"history_time": str(i), "history_value":"0" }
        energy_check_hot_data["history_year_list"].append(row_data)
    for i in range(1, 31):
        row_data = {"history_time": str(i), "history_value": "0"}
        energy_check_hot_data["history_month_list"].append(row_data)
    for i in range(0, 24):
        row_data = {"history_time": str(i), "history_value": "0"}
        energy_check_hot_data["history_day_list"].append(row_data)


    # # 测试数据
    test_data = {
        "check_name":"设备用热 {}".format(check_name),
        "hot":"178",
        "history_year_list":[
            {"history_time": "1", "history_value":"326" },
            {"history_time": "2", "history_value":"226" },
            {"history_time": "3", "history_value":"76" },
            {"history_time": "4", "history_value":"126" },
            {"history_time": "5", "history_value":"326" },
            {"history_time": "6", "history_value":"426" },
            {"history_time": "7", "history_value":"626" },
            {"history_time": "8", "history_value":"596" },
            {"history_time": "9", "history_value":"86" },
            {"history_time":"10", "history_value":"126" },
            {"history_time":"11", "history_value":"156" },
            {"history_time":"12", "history_value":"526" },
        ],
        "history_month_list":[
            {"history_time": "1", "history_value": "326"},
            {"history_time": "2", "history_value": "226"},
            {"history_time": "3", "history_value": "76"},
            {"history_time": "4", "history_value": "126"},
            {"history_time": "5", "history_value": "326"},
            {"history_time": "6", "history_value": "426"},
            {"history_time": "7", "history_value": "626"},
            {"history_time": "8", "history_value": "596"},
            {"history_time": "9", "history_value": "86"},
            {"history_time": "10", "history_value": "126"},
            {"history_time": "11", "history_value": "156"},
            {"history_time": "12", "history_value": "526"},
            {"history_time": "13", "history_value": "526"},
            {"history_time": "14", "history_value": "526"},
            {"history_time": "15", "history_value": "526"},
            {"history_time": "16", "history_value": "526"},
            {"history_time": "17", "history_value": "526"},
            {"history_time": "18", "history_value": "526"},
            {"history_time": "19", "history_value": "526"},
            {"history_time": "20", "history_value": "326"},
            {"history_time": "21", "history_value": "426"},
            {"history_time": "22", "history_value": "526"},
            {"history_time": "23", "history_value": "526"},
            {"history_time": "24", "history_value": "526"},
            {"history_time": "25", "history_value": "526"},
            {"history_time": "26", "history_value": "526"},
            {"history_time": "27", "history_value": "526"},
            {"history_time": "28", "history_value": "526"},
            {"history_time": "29", "history_value": "526"},
            {"history_time": "30", "history_value": "526"},
        ],
        "history_day_list":[
            {"history_time": "1", "history_value": "326"},
            {"history_time": "2", "history_value": "226"},
            {"history_time": "3", "history_value": "76"},
            {"history_time": "4", "history_value": "126"},
            {"history_time": "5", "history_value": "326"},
            {"history_time": "6", "history_value": "426"},
            {"history_time": "7", "history_value": "626"},
            {"history_time": "8", "history_value": "596"},
            {"history_time": "9", "history_value": "86"},
            {"history_time": "10", "history_value": "126"},
            {"history_time": "11", "history_value": "156"},
            {"history_time": "12", "history_value": "526"},
            {"history_time": "13", "history_value": "526"},
            {"history_time": "14", "history_value": "526"},
            {"history_time": "15", "history_value": "526"},
            {"history_time": "16", "history_value": "526"},
            {"history_time": "17", "history_value": "526"},
            {"history_time": "18", "history_value": "426"},
            {"history_time": "19", "history_value": "436"},
            {"history_time": "20", "history_value": "526"},
            {"history_time": "21", "history_value": "226"},
            {"history_time": "22", "history_value": "126"},
            {"history_time": "23", "history_value": "226"},
            {"history_time": "0", "history_value": "26"},
        ]
    }
    # return test_data
    return energy_check_hot_data



def get_device_ac_data(check_id):
    '''
    设备通用查询接口，使用唯一id 查询设备信息
    :return: dict
    '''
    check_name = get_device_name_by_id(check_id)

    # # 测试数据
    if check_id[0] == 'a':
        test_data = {
            "device_name":"空调-风机盘管，{}".format(check_name),
            "device_pic":"ac_wind.jpg",
            "device_sn":"ABC123",
            "device_factory":"西门子",
            "device_version":"cv100",
            "device_location":"1号楼1层",
            "device_info":[
                {
                    "device_info_name":"风量",
                    "device_info_value":"611m3",
                }
            ],
            "device_status":[
                {
                    "device_status_name":"室内温度",
                    "device_status_value":"23摄氏度",
                },
                {
                    "device_status_name":"冷水阀开关状态",
                    "device_status_value":"on",
                },
                {
                    "device_status_name":"报警信息",
                    "device_status_value":"无故障",
                }
            ]
        }
    else:
        test_data = {
            "device_name":"空调-水泵，{}".format(check_id),
            "device_pic":"ac_water_pump.jpg",
            "device_sn":"ABC123",
            "device_factory":"西门子",
            "device_version":"cv100",
            "device_location":"1号楼2层",
            "device_info":[
                {
                    "device_info_name":"扬程",
                    "device_info_value":"126m",
                },
                {
                    "device_info_name":"流量",
                    "device_info_value":"216m3",
                },
                {
                    "device_info_name":"功率",
                    "device_info_value":"3000w",
                }
            ],
            "device_status":[
                {
                    "device_status_name":"开关状态",
                    "device_status_value":"on",
                },
                {
                    "device_status_name":"报警信息",
                    "device_status_value":"无故障",
                }
            ]
        }
    return test_data

def get_device_ea_data(check_id):
    '''
    设备通用查询接口，使用唯一id 查询设备信息
    :return: dict
    '''
    check_name = get_name_by_id(check_id)

    # # 测试数据
    if check_id[0] == 'a':
        test_data = {
            "device_name": "智能插座，{}".format(check_name),
            "device_pic": "switch01.jpg",
            "device_sn": "ABC123{}".format(check_name),
            "device_factory": "小米",
            "device_version": "小米智能插座",
            "device_location": "1号楼2层控制室",
            "device_info": [
                {
                    "device_info_name": "插座类型",
                    "device_info_value": "5孔",
                },
            ],
            "device_status": [
                {
                    "device_status_name": "开关状态",
                    "device_status_value": "on",
                },
                {
                    "device_status_name": "实时电流",
                    "device_status_value": "20mA",
                }
            ]
        }
    else:
        test_data = {
            "device_name": "其他电器，{}".format(check_name),
            "device_pic": "ea01.jpg",
            "device_sn": "ABC123{}".format(check_name),
            "device_factory": "霍尼韦尔",
            "device_version": "",
            "device_location": "1号楼3层控制室",
            "device_info": [
                {
                    "device_info_name": "类型1",
                    "device_info_value": "设备1",
                },
                {
                    "device_info_name": "类型2",
                    "device_info_value": "设备2",
                },
            ],
            "device_status": [
                {
                    "device_status_name": "开关状态",
                    "device_status_value": "on",
                },
            ]
        }
    return test_data


def get_security_camera_data(check_id):
    '''
    安防摄像头设备查询接口，使用唯一id 查询设备信息
    :return: dict
    '''
    check_name = get_name_by_id(check_id)

    # # 测试数据
    test_data = {
        "device_name":"安防摄像头1，{}".format(check_name),
        "device_pic":"cam01.jpg",
        "device_sn":"ABC123",
        "device_factory":"西门子",
        "device_version":"cv100",
        "device_location":"1号楼1层",
        "device_status":[
            {
                "device_status_name":"摄像头状态",
                "device_status_value":"on",
            }
        ],
        "camera_config":{
            "server_ip":"207.101.67.182",
            "user_name":"loadmin",
            "password":"d6bf4bb9a66419380a",
            "cam_code":"EC2004-139_1",
        }
    }
    return test_data


def get_security_device_data(check_id):
    '''
    安防设备查询接口，使用唯一id 查询设备信息
    :return: dict
    '''
    check_name = get_name_by_id(check_id)
    # # 测试数据
    test_data = {
        "device_name":"红外报警器{}".format(check_name),
        "device_pic":"Infrared_alarm01.jpg",
        "device_sn":"ABC123",
        "device_factory":"西门子",
        "device_version":"ia1001",
        "device_location":"1号楼1层",
        "device_status":[
            {
                "device_status_name":"运行状态",
                "device_status_value":"正常",
            },
        ]
    }
    return test_data


def get_fire_equipment_data(check_id):
    '''
    消防设备查询接口，使用唯一id 查询设备信息
    :return: dict
    '''
    check_name = get_name_by_id(check_id)

    # # 测试数据
    test_data = {
        "device_name":"消防报警器 {}".format(check_name),
        "device_pic":"fire_alarm01.jpg",
        "device_sn":"ABC123",
        "device_factory":"西门子",
        "device_version":"fa1032",
        "device_location":"1号楼1层",
        "device_status":[
            {
                "device_status_name":"运行状态",
                "device_status_value":"正常",
            },
        ]
    }
    return test_data


def update_user_data(user_data_dict):
    '''
    :param user_data_dict:
    :return:
    '''
    # # 测试数据
    test_data = {
        "password": user_data_dict.get('password'),
        "nickname": user_data_dict.get('nickname'),
        "phone": user_data_dict.get('phone'),
    }
    return test_data


def update_area_data(data_dict):
    '''
    :param data_dict:
    :return:
    '''
    # # 测试数据
    test_data = {
        "land_area": data_dict.get('land_area'),
        "buildings_amount": data_dict.get('buildings_amount'),
        "buildings_area": data_dict.get('buildings_area'),
        "floor_area_ratio": data_dict.get('floor_area_ratio'),
        "greening_rate": data_dict.get('greening_rate'),
        "company_amount": data_dict.get('company_amount'),
        "area_people_amount": data_dict.get('area_people_amount'),
    }
    return test_data

def update_building_data(data_dict):
    '''
    :param data_dict:
    :return:
    '''
    # # 测试数据
    test_data ={
        "building_id": data_dict.get('building_id'),
        "building_name": data_dict.get('building_name'),
        "building_function": data_dict.get('building_function'),
        "building_area": data_dict.get('building_area'),
        "building_time": data_dict.get('building_time'),
        "building_height": data_dict.get('building_height'),
        "building_floors": data_dict.get('building_floors'),
    }
    return test_data

def update_room_data(data_dict):
    '''
    :param data_dict:
    :return:
    '''
    # # 测试数据
    test_data ={
        "room_id": data_dict.get('room_id'),
        "room_name": data_dict.get('room_name'),
    }
    return test_data

def update_property_data(data_dict):
    '''
    :param data_dict:
    :return:
    '''
    # # 测试数据
    test_data ={
        "date": data_dict.get('date'),
        "gas_boiler": data_dict.get('value1'),
        "gas_kitchen": data_dict.get('value2'),
        "value1": data_dict.get('value3'),
        "value2": data_dict.get('value4'),
    }
    return test_data

if __name__ == '__main__':
    print('---', get_name_by_id('room_a2f228'))
