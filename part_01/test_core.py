#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 21:16:00 2020

@author: flpbraun
"""

import sys
path = '/home/flpbraun/PS_Linx/'
if path not in sys.path:
   sys.path.insert(0, path)
from flask import json
from prod_app import app as application
import pytest

@pytest.fixture
def client(request):
    test_client = application.test_client()

    def teardown():
        pass 
    
    request.addfinalizer(teardown)
    return test_client

def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')

def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))

def test_home(client):
    response = client.get('/')
    assert b'Processo Seletivo Linx Impulse by Felipe Braun \n' in response.data
    
def test_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    
def test_json1(client):
    response = post_json(client, '/products', {'id': 'test_id', 'name':'test_name'})
    assert response.status_code == 200
    assert b'Succesfully Posted! \n' in response.data

def test_json2(client):
    response = post_json(client, '/products', {'id': 'test_id', 'name':'test_name'})
    assert response.status_code == 200
    assert b'Permission denied! Try again later. \n' in response.data
