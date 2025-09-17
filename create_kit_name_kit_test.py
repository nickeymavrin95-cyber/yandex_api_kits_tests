import sender_stand_request
import data


def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    assert response.status_code == 201
    auth_token = response.json().get("authToken")
    assert auth_token != "", "AuthToken не должен быть пустым"
    return auth_token


def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    

def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

# Тест 1: Допустимое количество символов (1)
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = {
    "name": "a"
    }
    positive_assert(kit_body)

# Тест 2: Допустимое количество символов (511)
def test_create_kit_511_letters_in_name_get_success_response():
    kit_body = {    "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
    positive_assert(kit_body)

# Тест 3: Количество символов меньше допустимого (0)
def test_create_kit_0_letters_in_name_get_error_response():
    kit_body = {
        "name": ""
    }
    negative_assert_code_400(kit_body)

# Тест 4: Количество символов больше допустимого (512)
def test_create_kit_512_letters_in_name_get_error_response():
    kit_body = {  "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
    negative_assert_code_400(kit_body)

# Тест 5: Разрешены английские буквы
def test_create_kit_english_letters_in_name_get_success_response():
    kit_body = {
        "name": "QWErty"
    }
    positive_assert(kit_body)

# Тест 6: Разрешены русские буквы
def test_create_kit_russian_letters_in_name_get_success_response():
    kit_body = {
        "name": "Мария"
    }
    positive_assert(kit_body)

# Тест 7: Разрешены спецсимволы
def test_create_kit_special_symbols_in_name_get_success_response():
    kit_body = {
        "name": r"№%@,"
    }
    positive_assert(kit_body)

# Тест 8: Разрешены пробелы
def test_create_kit_spaces_in_name_get_success_response():
    kit_body = {
        "name": " Человек и КО "
    }
    positive_assert(kit_body)

# Тест 9: Разрешены цифры
def test_create_kit_numbers_in_name_get_success_response():
    kit_body = {
        "name": "123"
        }
    positive_assert(kit_body)

# Тест 10: Параметр не передан в запросе
def test_create_kit_no_name_get_error_response():
    kit_body = {}  
    negative_assert_code_400(kit_body)

# Тест 11: Передан другой тип параметра (число вместо строки)
def test_create_kit_number_type_name_get_error_response():
    kit_body = {
        "name": 123 
    }
    negative_assert_code_400(kit_body)