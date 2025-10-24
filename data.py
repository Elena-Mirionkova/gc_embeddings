from generators import *
import os

class ResponseCodes:
    bad_params = 422
    bad_request = 400
    auth_error = 401
    ok = 200
    not_found = 404
    too_many_requests = 429

class Responses:
    bad_params = 422
    bad_request = 400
    auth_error = {"status": 401, "message": "Unauthorized"}
    not_found = {"status": 404, "message": "No such model"}
    too_many_requests = {"status": 429, "message": "Too many requests"}

class SecurityData:
    # Ключ авторизации для получения токена https://developers.sber.ru/docs/ru/gigachat/api/reference/rest/post-token
    authorization_key = os.getenv("AUTH_KEY")
    session_id = generate_uuid()
    scope = 'GIGACHAT_API_PERS'

class RequestData:
    model = "GigaChat:1.0.26.20"
    incorrect_model = "ChatGPT:1.0"
    role = "user"
    incorrect_role = "panda"
    content = "Погода в Москве в ближайшие три дня"
    temperature = 1
    top_p = 1
    stream = False
    max_tokens = 100
    repetition_penalty = 1
    update_interval = 0
    x_client = generate_uuid()
    x_request = generate_uuid()
    x_session = generate_uuid()
    content_type = "application/json"
    incorrect_token = "gdfgtoirdotgpospofsp0wiofpseorf647327kdhjghdlz"

repetitions_limit = 100


