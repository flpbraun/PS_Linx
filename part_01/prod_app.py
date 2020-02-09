#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:18:45 2020

@author: flpbraun
"""

from flask import Flask, jsonify, request
from datetime import datetime, timedelta

app = Flask(__name__)

products = []

@app.route('/') 
def home():
    return 'Processo Seletivo Linx Impulse by Felipe Braun \n'

# GET 
@app.route('/products')
def get_products():
    return jsonify(products)

# POST 
@app.route('/products', methods=['POST'])
def create_product():
    request_data = request.get_json()
    
    new_item = {
            'id': request_data['id'],
            'name': request_data['name'],
            'DateTime': datetime.now()
            }
    if any(product.get('id') == new_item['id'] for product in products) and\
    any(product.get('name') == new_item['name'] for product in products) and\
    any(product.get('DateTime') > (new_item['DateTime'] - timedelta(minutes = 10)) for product in products):
        return 'Permission denied! Try again later. \n'
    else:
        products.append(new_item)
        return 'Succesfully Posted! \n'

if __name__ == '__main__':
    app.run(port=5000)

