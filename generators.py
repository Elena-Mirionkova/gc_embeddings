from faker import Faker

fake = Faker('ru_RU')

def generate_request():
    return fake.text(20)

def generate_requests():
    return fake.texts(nb_texts=5, max_nb_chars=20)

def generate_uuid():
    return fake.uuid4()
