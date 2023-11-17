import requests
import pytest

@pytest.fixture
def data_api():

    data_api = {
        'api_key':'9620c26a3dfff5a2e5f0d010ced23acc',
        'base_url':'https://api.openweathermap.org/data/2.5/weather?',
        'base_Not_Found_url':'https://api.openweathermap.org/dataa/2.5/weather?',
        'wrong_api_key':'9620c26a3dfff5a2e5f0d010ced23ac',
        'region':'Campinas,BR',
        'complete_url':'https://api.openweathermap.org/data/2.5/weather?appid=9620c26a3dfff5a2e5f0d010ced23acc&q=Campinas,BR',
        'complete_Bad_Request_url':'https://api.openweathermap.org/data/2.5/weather?appid=9620c26a3dfff5a2e5f0d010ced23acc&q=Campinas,BR'
    }
    return data_api


def test_get_code_response_OK(data_api):
    response = requests.get(data_api['complete_url'])
    assert response.status_code == 200

def test_get_code_response_BadRequest(data_api):
    try:
        requests.get(data_api['complete_Bad_Request_url'])
    except Exception as e:
        response_code = 400
        assert response_code==400

def test_get_code_response_Unauthorized(data_api):
    response = requests.get(data_api['base_url']+'appid=' + data_api['wrong_api_key'] +'&q='+data_api['region'])
    assert response.status_code == 401

def test_get_code_response_Not_Found(data_api):
    response = requests.get(data_api['base_Not_Found_url']+'appid=' + data_api['api_key'] +'&q='+data_api['region'])
    assert response.status_code == 404

'''
def test_request_too_many_resquests():

    def getResponseTooManyRequests(url):
        response = requests.get(url)
        print(response.status_code)
        if  response.status_code == 429:
            assert response.status_code == 429:

    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
            while True:
                pool.submit(getResponseTooManyRequests,data_api['base_wrongUrl'])
'''