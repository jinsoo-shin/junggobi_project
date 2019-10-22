#-*- coding:utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import urllib.request
import re
import pandas as pd
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}
def save_product():
    with open('product.csv', 'r') as read_data:
        read_data = list(read_data)
        request_data = {'product': []}
        for i in range(len(read_data)):
            # for i in range(10) :
            print("#############################################")
            read_data[i] = read_data[i].replace("\n", "").replace("  ", " ")
            read_line = read_data[i].split(',')
            print(read_line)
            id = read_line[0]
            category = read_line[1]
            manufacturer = read_line[2]
            model_name = read_line[3]
            generation = read_line[4]
            display = read_line[5]
            release_date = read_line[6]
            request_data['product'].append({
                'id':id,
                'category': category,
                'manufacturer': manufacturer,
                'model_name': model_name,
                'display': display,
                'generation': generation,
                'release_date': release_date,
            })
    print(request_data)
    response = requests.post(API_URL + 'api/index/', data=json.dumps(request_data), headers=headers)


def save_tablet():
    with open('tablet.csv', 'r') as read_data:
        read_data = list(read_data)
        request_data = {'tablet': []}
        for i in range(len(read_data)):
            # for i in range(10) :
            print("#############################################")
            read_data[i] = read_data[i].replace("\n", "").replace("  ", " ")
            read_line = read_data[i].split(',')
            print(read_line)
            product_id=read_line[0]
            key_name = read_line[1]
            cellular = read_line[2]
            storage = read_line[3]
            price = read_line[4]
            query = read_line[5]
            request_data['tablet'].append({
                'product_id':product_id,
                'key_name': key_name,
                'cellular': cellular,
                'storage': storage,
                'price': price,
                'query': query,
            })
    print(request_data)
    response = requests.post(API_URL + 'api/index/', data=json.dumps(request_data), headers=headers)


if __name__ == '__main__':
#    save_product()
   save_tablet()