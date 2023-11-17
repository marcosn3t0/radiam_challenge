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
    region = 'Campinas,BR'
    complete_url = base_url + 'appid=' + api_key + '&q=' + region
    return complete_url

@pytest.mark.parametrize('exclude,sunrise,pressure', 
[('current','942346205','1014'),
('current','2023-11-17','1000'),
('current','-123231','-1000'),
('current','','')])
def test_current_date_weather(complete_url,exclude,sunrise,pressure):
    response = requests.get(complete_url+'&exclude='+exclude+'&sunrise='+sunrise+'&pressure='+pressure)
    assert response.status_code == 200

@pytest.mark.parametrize('exclude,temp,clouds',
[('hourly','292.01','64'),
('hourly','-12','54'),
('hourly','',''),
('hourly','-12','-54.0')])
def test_hourly_date_weather(complete_url,exclude,temp,clouds):
    response = requests.get(complete_url+'&exclude='+exclude+'&temp='+temp+'&clouds='+clouds)
    assert response.status_code == 200


@pytest.mark.parametrize('exclude,dt,precipitation', 
[('minutely','1684926645','-1'),
('minutely','-1684926627','0'),
('minutely','-123231','1000'),
('minutely','','')])
def test_minutely_date_weather(complete_url,exclude,dt,precipitation):
    response = requests.get(complete_url+'&exclude='+exclude+'&dt='+dt+'&precipitation='+precipitation)
    assert response.status_code == 200