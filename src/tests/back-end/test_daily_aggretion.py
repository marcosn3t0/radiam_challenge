import os
import sys
sys.path.insert(0,os.getcwd()+'\\src')
import requests
from multiprocessing.pool import Pool
import pytest


@pytest.fixture
def complete_url():
    api_key = '9620c26a3dfff5a2e5f0d010ced23acc'
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + 'appid=' + api_key
    return complete_url

@pytest.mark.parametrize('dt,region,temperature', 
    [('2023-11-17','Africa','afternoon'), 
    ('2022-01-21','Japan','min'), 
    ('2025-08-01','Paraguay','max'),
    ('1998-09-06','Bolivia','morning'),
    ('1988-01-18','Cañada','')])
def test_daily_aggretion_weather(complete_url,region,dt,temperature):
    response = requests.get(complete_url+'&date='+dt+'&temperature='+temperature+'&q=' + region)
    assert response.json()['name'] == region
    assert response.status_code == 200

