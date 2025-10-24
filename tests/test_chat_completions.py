import requests
import pytest
import allure
import json
from data import *
from urls import *

class TestChatCompletions:

    @allure.title('Позитивный тест на получение ответа.')
    def test_reply_to_the_message(self, token):
        url = main_url + completions   
        data = json.dumps({
            "model": RequestData.model,
            "messages": [
                {
                "role": RequestData.role,
                "content": RequestData.content
                }
            ],
            "temperature": RequestData.temperature,
            "top_p": RequestData.top_p,
            "stream": RequestData.stream,
            "max_tokens": RequestData.max_tokens,
            "repetition_penalty": RequestData.repetition_penalty,
            "update_interval": RequestData.update_interval
        })
        headers = {
            'X-Client-ID': RequestData.x_client,
            'X-Request-ID': RequestData.x_request,
            'X-Session-ID': RequestData.x_session,
            'Content-Type': RequestData.content_type,
            'Authorization': "Bearer " + token
            }

        with allure.step(f'POST запрос к {url} с данными {data}'):
            response = requests.post(url, headers=headers, data=data, verify=False)
        r = response.json()
        assert response.status_code == ResponseCodes.ok and len(r["choices"][0]["message"]["content"]) > 0

    @allure.title('Получаем ошибку 400.')
    def test_bad_request(self, token):
        url = main_url + completions   
        data = ""
        headers = {
            'X-Client-ID': RequestData.x_client,
            'X-Request-ID': RequestData.x_request,
            'X-Session-ID': RequestData.x_session,
            'Content-Type': RequestData.content_type,
            'Authorization': "Bearer " + token
            }

        with allure.step(f'POST запрос к {url} с данными {data}'):
            response = requests.post(url, headers=headers, data=data, verify=False)
        r = response.json()

        assert response.status_code == ResponseCodes.bad_request and r["status"] == Responses.bad_request
    

    @allure.title('Получаем ошибку 401.')
    def test_unauthorized(self):
        url = main_url + completions   
        data = json.dumps({
            "model": RequestData.model,
            "messages": [
                {
                "role": RequestData.role,
                "content": RequestData.content
                }
            ],
            "temperature": RequestData.temperature,
            "top_p": RequestData.top_p,
            "stream": RequestData.stream,
            "max_tokens": RequestData.max_tokens,
            "repetition_penalty": RequestData.repetition_penalty,
            "update_interval": RequestData.update_interval
        })
        headers = {
            'X-Client-ID': RequestData.x_client,
            'X-Request-ID': RequestData.x_request,
            'X-Session-ID': RequestData.x_session,
            'Content-Type': RequestData.content_type,
            'Authorization': "Bearer " + RequestData.incorrect_token
            }

        with allure.step(f'POST запрос к {url} с данными {data}'):
            response = requests.post(url, headers=headers, data=data, verify=False)
        r = response.json()
        assert response.status_code == ResponseCodes.auth_error and r == Responses.auth_error
    

    @allure.title('Получаем ошибку 404.')
    def test_not_found(self, token):
        url = main_url + completions   
        data = json.dumps({
            "model": RequestData.incorrect_model,
            "messages": [
                {
                "role": RequestData.role,
                "content": RequestData.content
                }
            ],
            "temperature": RequestData.temperature,
            "top_p": RequestData.top_p,
            "stream": RequestData.stream,
            "max_tokens": RequestData.max_tokens,
            "repetition_penalty": RequestData.repetition_penalty,
            "update_interval": RequestData.update_interval
        })
        headers = {
            'X-Client-ID': RequestData.x_client,
            'X-Request-ID': RequestData.x_request,
            'X-Session-ID': RequestData.x_session,
            'Content-Type': RequestData.content_type,
            'Authorization': "Bearer " + token
            }

        with allure.step(f'POST запрос к {url} с данными {data}'):
            response = requests.post(url, headers=headers, data=data, verify=False)
        r = response.json()
        assert response.status_code == ResponseCodes.not_found and r == Responses.not_found
    

    @allure.title('Получаем ошибку 422.')
    def test_invalid_params(self, token):
        url = main_url + completions   
        data = json.dumps({
            "model": RequestData.model,
            "messages": [
                {
                "role": RequestData.incorrect_role,
                "content": RequestData.content
                }
            ],
            "temperature": RequestData.temperature,
            "top_p": RequestData.top_p,
            "stream": RequestData.stream,
            "max_tokens": RequestData.max_tokens,
            "repetition_penalty": RequestData.repetition_penalty,
            "update_interval": RequestData.update_interval
        })
        headers = {
            'X-Client-ID': RequestData.x_client,
            'X-Request-ID': RequestData.x_request,
            'X-Session-ID': RequestData.x_session,
            'Content-Type': RequestData.content_type,
            'Authorization': "Bearer " + token
            }

        with allure.step(f'POST запрос к {url} с данными {data}'):
            response = requests.post(url, headers=headers, data=data, verify=False)
        r = response.json()
        assert response.status_code == ResponseCodes.bad_params and r["status"] == Responses.bad_params


"""
    @allure.title('Получаем ошибку 429.')
    def test_too_many_requests(self, token):
        url = main_url + completions   
        data = json.dumps({
            "model": RequestData.model,
            "messages": [
                {
                "role": RequestData.role,
                "content": RequestData.content
                }
            ],
            "temperature": RequestData.temperature,
            "top_p": RequestData.top_p,
            "stream": RequestData.stream,
            "max_tokens": RequestData.max_tokens,
            "repetition_penalty": RequestData.repetition_penalty,
            "update_interval": RequestData.update_interval
        })
        headers = {
            'X-Client-ID': RequestData.x_client,
            'X-Request-ID': RequestData.x_request,
            'X-Session-ID': RequestData.x_session,
            'Content-Type': RequestData.content_type,
            'Authorization': "Bearer " + token
            }

        i = 0
        with allure.step(f'POST запрос к {url} с данными {data}. Повтор {repetitions_limit} раз'):
            response = requests.post(url, headers=headers, data=data, verify=False)
        while response.status_code == ResponseCodes.ok and i < repetitions_limit:
            response = requests.post(url, headers=headers, data=data, verify=False)
            i += 1
        
        assert response.status_code == ResponseCodes.too_many_requests
"""        
