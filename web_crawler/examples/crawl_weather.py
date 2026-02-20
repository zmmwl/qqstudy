# -*- coding: utf-8 -*-
"""
示例2：爬取天气信息
====================

这是一个模拟的天气爬虫示例
由于实际天气网站API经常变化，这里使用模拟数据演示

演示内容：
- 如何爬取结构化数据
- 如何处理JSON API
- 如何格式化输出天气信息

运行方法：
python crawl_weather.py
"""

import requests
import json
import os
from datetime import datetime


def get_weather_from_api(city="Beijing"):
    """
    从天气API获取数据（使用免费的Open-Meteo API）

    参数说明：
        city (str): 城市名称（英文）

    返回值：
        dict: 天气数据

    调用示例：
        weather = get_weather_from_api("Beijing")
        weather = get_weather_from_api("Shanghai")
    """
    print(f"\n🌤️ 正在获取 {city} 的天气信息...")

    # 城市坐标（经纬度）
    city_coords = {
        "Beijing": {"lat": 39.9042, "lon": 116.4074},
        "Shanghai": {"lat": 31.2304, "lon": 121.4737},
        "Guangzhou": {"lat": 23.1291, "lon": 113.2644},
        "Shenzhen": {"lat": 22.5431, "lon": 114.0579},
        "Hangzhou": {"lat": 30.2741, "lon": 120.1551},
    }

    if city not in city_coords:
        print(f"❌ 不支持的城市: {city}")
        print(f"支持的城市: {list(city_coords.keys())}")
        return None

    coords = city_coords[city]

    # Open-Meteo API（免费，无需API密钥）
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": coords["lat"],
        "longitude": coords["lon"],
        "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
        "timezone": "Asia/Shanghai"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return {
                "city": city,
                "data": data
            }
        else:
            print(f"❌ API返回状态码: {response.status_code}")
            return None

    except Exception as e:
        print(f"❌ 获取天气失败: {e}")
        return None


def parse_weather_code(code):
    """
    解析天气代码

    参数说明：
        code (int): WMO天气代码

    返回值：
        str: 天气描述（中文）
    """
    weather_codes = {
        0: "晴朗",
        1: "基本晴朗", 2: "部分多云", 3: "阴天",
        45: "有雾", 48: "雾凇",
        51: "小毛毛雨", 53: "中毛毛雨", 55: "大毛毛雨",
        61: "小雨", 63: "中雨", 65: "大雨",
        71: "小雪", 73: "中雪", 75: "大雪",
        80: "小阵雨", 81: "中阵雨", 82: "大阵雨",
        95: "雷暴", 96: "雷暴伴小冰雹", 99: "雷暴伴大冰雹",
    }
    return weather_codes.get(code, "未知天气")


def display_weather(weather_info):
    """
    格式化显示天气信息

    参数说明：
        weather_info (dict): 天气数据
    """
    if not weather_info:
        print("❌ 没有天气数据")
        return

    city = weather_info["city"]
    data = weather_info["data"]["current"]

    # 解析数据
    temp = data.get("temperature_2m", "N/A")
    humidity = data.get("relative_humidity_2m", "N/A")
    weather_code = data.get("weather_code", 0)
    wind_speed = data.get("wind_speed_10m", "N/A")

    weather_desc = parse_weather_code(weather_code)

    # 显示
    print("\n" + "=" * 50)
    print(f"📍 城市: {city}")
    print("=" * 50)
    print(f"🌡️  温度: {temp}°C")
    print(f"💧 湿度: {humidity}%")
    print(f"☁️  天气: {weather_desc}")
    print(f"💨 风速: {wind_speed} km/h")
    print(f"🕐 更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)


def get_mock_weather(city="北京"):
    """
    获取模拟天气数据（当网络不可用时使用）

    参数说明：
        city (str): 城市名称

    返回值：
        dict: 模拟的天气数据
    """
    import random

    weathers = ["晴", "多云", "阴", "小雨", "大雨", "雪"]

    return {
        "city": city,
        "temperature": random.randint(-5, 35),
        "humidity": random.randint(30, 90),
        "weather": random.choice(weathers),
        "wind": f"{random.randint(1, 20)} km/h",
        "update_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }


def display_mock_weather(weather):
    """
    显示模拟天气

    参数说明：
        weather (dict): 模拟天气数据
    """
    print("\n" + "=" * 50)
    print(f"📍 城市: {weather['city']} (模拟数据)")
    print("=" * 50)
    print(f"🌡️  温度: {weather['temperature']}°C")
    print(f"💧 湿度: {weather['humidity']}%")
    print(f"☁️  天气: {weather['weather']}")
    print(f"💨 风速: {weather['wind']}")
    print(f"🕐 更新时间: {weather['update_time']}")
    print("=" * 50)
    print("\n⚠️  这是模拟数据，仅用于演示")


def save_weather_to_file(weather_info, filepath):
    """
    保存天气数据到文件

    参数说明：
        weather_info (dict): 天气数据
        filepath (str): 保存路径
    """
    # 添加保存时间
    weather_info["saved_at"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(weather_info, f, ensure_ascii=False, indent=2)

    print(f"✅ 天气数据已保存: {filepath}")


def crawl_multiple_cities(cities):
    """
    爬取多个城市的天气

    参数说明：
        cities (list): 城市列表

    返回值：
        list: 所有城市的天气数据
    """
    all_weather = []

    for city in cities:
        weather = get_weather_from_api(city)
        if weather:
            all_weather.append(weather)

    return all_weather


def main():
    """
    主函数
    """
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║           🌤️  天气信息爬虫  🌤️                           ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

【说明】
本示例演示如何爬取天气API数据
使用免费的 Open-Meteo API（无需注册）

【支持的城市】
Beijing（北京）, Shanghai（上海）, Guangzhou（广州）
Shenzhen（深圳）, Hangzhou（杭州）
    """)

    # 创建保存目录
    save_dir = "/mnt/c/dev/python/qqstudy/web_crawler/data"
    os.makedirs(save_dir, exist_ok=True)

    print("\n请选择操作：")
    print("1. 获取单个城市天气")
    print("2. 获取所有支持城市天气")
    print("3. 使用模拟数据（离线演示）")

    choice = input("\n请输入选项 (1/2/3): ").strip()

    if choice == '1':
        # 单个城市
        city = input("请输入城市名称（英文，如Beijing）: ").strip()
        if not city:
            city = "Beijing"

        weather = get_weather_from_api(city)
        if weather:
            display_weather(weather)

            # 保存
            save = input("\n是否保存到文件？(y/n): ").lower()
            if save == 'y':
                filepath = os.path.join(save_dir, f"weather_{city}.json")
                save_weather_to_file(weather, filepath)

    elif choice == '2':
        # 所有城市
        cities = ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Hangzhou"]
        all_weather = crawl_multiple_cities(cities)

        print("\n" + "=" * 60)
        print("📊 所有城市天气汇总")
        print("=" * 60)

        for weather in all_weather:
            data = weather["data"]["current"]
            temp = data.get("temperature_2m", "N/A")
            weather_desc = parse_weather_code(data.get("weather_code", 0))
            print(f"{weather['city']:15} | {temp:5}°C | {weather_desc}")

        # 保存
        filepath = os.path.join(save_dir, "weather_all.json")
        save_weather_to_file(all_weather, filepath)

    else:
        # 模拟数据
        city = input("请输入城市名称: ").strip()
        if not city:
            city = "北京"

        weather = get_mock_weather(city)
        display_mock_weather(weather)

    print("\n" + "=" * 60)
    print("🎉 程序执行完毕！")
    print("=" * 60)


if __name__ == "__main__":
    main()
