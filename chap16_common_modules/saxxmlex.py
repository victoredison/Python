#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#An exercise to parse the XML response from weatherapi.com

__author__ = 'victor yu'

from xml.parsers.expat import ParserCreate
from urllib import request


class WeatherSaxHandler:
    def __init__(self):
        self.weather_data = {
            'city': '',
            'weather': {
                'condition': '',
                'temperature': 0,
                'wind': 0
            }
        }
        self.current_element = ''

    
    def start_element(self, name, attrs):
        self.current_element = name

    
    def end_element(self, name):
        self.current_element = ''

    
    def char_data(self, data):
        
        if self.current_element == 'name':
            self.weather_data['city'] = data.strip()
        
        elif self.current_element == 'text':
            self.weather_data['weather']['condition'] = data.strip()
        
        elif self.current_element == 'temp_c':
            self.weather_data['weather']['temperature'] = float(data.strip())
        
        elif self.current_element == 'wind_kph':
            self.weather_data['weather']['wind'] = float(data.strip())

def parseXml(xml_str):
    
    handler = WeatherSaxHandler()
    parser = ParserCreate()

    
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data

    
    parser.Parse(xml_str)
    
    return handler.weather_data

# Test:
URL = 'https://api.weatherapi.com/v1/current.xml?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no'

# Fetch the XML data
with request.urlopen(URL, timeout=4) as f:
    data = f.read()

# Parse the XML data
result = parseXml(data.decode('utf-8'))

# Assert and print the result
print(f"Parsed data: {result}")
assert result['city'] == 'Beijing'

