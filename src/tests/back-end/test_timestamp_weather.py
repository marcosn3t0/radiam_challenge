import os
import sys
sys.path.insert(0,os.getcwd()+'\\src')
import requests
import pytest


@pytest.fixture
def complete_url():
    api_key = '9620c26a3dfff5a2e5f0d010ced23acc'
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + 'appid=' + api_key

    return complete_url

@pytest.mark.parametrize('dt,region',
[('-2497593445','London'),
('1699458967','Spain'),
('1736351767','China')])
def test_timestamp_weather(complete_url,dt,region):
    response = requests.get(complete_url+'&dt='+dt+ '&q=' + region)
    assert response.json()['name'] == region
    assert response.status_code == 200

