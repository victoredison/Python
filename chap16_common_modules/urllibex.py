#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# an urllib exercise 

__author__ = 'victor yu'



from urllib import request
import json

def fetch_data(url):

    req= request.Request(url)
    with request.urlopen(req) as response:
        data = response.read() 
        #The data returned by the fetch_data function is a string 
        #convert the JSON response (which is a string) into a Python dictionary using the json module.
    return json.loads(data.decode())

# 测试
URL = 'https://api.weatherapi.com/v1/current.json?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no'
data = fetch_data(URL)
print(data)
assert data['location']['name'] == 'Beijing'
print('ok')