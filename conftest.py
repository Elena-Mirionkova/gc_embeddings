import pytest
import requests
import allure
from data import *
from urls import *

@allure.title('Получаем токен авторизации')
@pytest.fixture(scope='class')
def token():
    url = auth_url + get_token
    auth_key = SecurityData.authorization_key
    rquid = SecurityData.session_id
    scope = SecurityData.scope
    
    headers = {
    'Authorization': 'Basic ' + auth_key,
    'RqUID': rquid,
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = 'scope=' + scope
    with allure.step(f'POST запрос к {url} с данными {data}'):
        response = requests.post(url, headers=headers, data=data, verify=False)
    r = response.json()
    return r["access_token"]
    
