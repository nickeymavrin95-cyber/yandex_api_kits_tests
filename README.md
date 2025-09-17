<p class="has-line-data" data-line-start="0" data-line-end="9">Структура проекта<br>
text<br>
project/<br>
<a href="http://configuration.py">configuration.py</a>      # Конфигурация URL и эндпоинтов<br>
<a href="http://data.py">data.py</a>              # Тестовые данные и заголовки<br>
sender_stand_request.py     # Функции для HTTP-запросов<br>
create_kit_name_kit_test.py     # Тестовые сценарии<br>
<a href="http://README.md">README.md</a>            # Документация<br>
.gitignore          # Исключаемые файлы из Git</p>
<p class="has-line-data" data-line-start="10" data-line-end="16">Назначение проекта<br>
Автотесты для проверки API создания наборов (kits) с различными валидациями:<br>
Проверка граничных значений длины имени (1, 511, 0, 512 символов)<br>
Тестирование разных типов символов (английские, русские, спецсимволы, цифры)<br>
Проверка обработки пробелов<br>
Валидация отсутствия параметра и неверного типа данных</p>
<p class="has-line-data" data-line-start="17" data-line-end="21">Зависимости<br>
Python 3.13.7<br>
Библиотека requests<br>
Библиотека pytest</p>
<p class="has-line-data" data-line-start="22" data-line-end="23">Запуск тестов</p>
<ol>
<li class="has-line-data" data-line-start="23" data-line-end="25">Установка зависимостей<br>
pip install requests pytest</li>
<li class="has-line-data" data-line-start="25" data-line-end="28">Запуск всех тестов<br>
pytest create_kit_name_kit_test.py -v</li>
</ol>
<p class="has-line-data" data-line-start="28" data-line-end="40">Список тестов<br>
+Создание набора с 1 символом в имени<br>
+Создание набора с 511 символами (максимально допустимо)<br>
-Создание набора с 0 символов (ожидается ошибка 400)<br>
-Создание набора с 512 символами (ожидается ошибка 400)<br>
+Создание набора с английскими буквами<br>
+Создание набора с русскими буквами<br>
+Создание набора со спецсимволами<br>
+Создание набора с пробелами<br>
+Создание набора с цифрами<br>
+Создание набора без параметра name (ожидается ошибка 400)<br>
-Создание набора с числом вместо строки (ожидается ошибка 400)</p>
<p class="has-line-data" data-line-start="41" data-line-end="43">Конфигурация<br>
Проект использует URL тестового стенда (необходимо прописать в <a href="http://configuration.py">configuration.py</a>)</p>
<p class="has-line-data" data-line-start="44" data-line-end="47">Эндпоинты:<br>
POST /api/v1/users/ - создание пользователя<br>
POST /api/v1/kits - создание набора</p>
<p class="has-line-data" data-line-start="48" data-line-end="52">Ожидаемые результаты:<br>
201 Created - для валидных данных<br>
400 Bad Request - для невалидных данных<br>
Все тесты должны проходить без ошибок</p>