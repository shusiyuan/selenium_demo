# -*- coding:utf-8 -*-
#获取中国天气网广东日温最高的城市列表
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.weather.com.cn/guangdong/index.shtml')
cities = driver.find_elements(By.XPATH,"//dt/a[contains(@title,'天气预报')]")
weathers = driver.find_elements(By.XPATH,"//div[@class='forecast']//a/span")
city_weather = {}
if len(cities) == len(weathers):
    for i in range(0,len(cities)):
        city_weather[cities[i].text] = int("".join(list(filter(str.isdigit,weathers[i].text))))
else:
    print("city长度为%d，weather长度为%d",len(cities),len(weathers))
    for i in cities:
        print(i.text)
#print (city_weather.items())
coldest_weather  = 0
coldest_city = ["广州"]
city_list = ''
for city in city_weather: #取得最高温
    if city_weather[city] > coldest_weather:
        coldest_weather = city_weather[city]
        coldest_city[0] = city
for city in city_weather: #兼容多个最高温
    if city_weather[city] == coldest_weather and coldest_city[0] != city:
        coldest_city.append(city)
if len(coldest_city) > 1: #列表格式化输出
    for i in range(0,len(coldest_city)):
        if i != len(coldest_city)-1:
            city_list = city_list + coldest_city[i] + '、'
        else:
            city_list = city_list + coldest_city[i]

print("本日广东省日温最高的城市为{city}，最高温为{weather}℃。".format(city = city_list,weather = coldest_weather))

