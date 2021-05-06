# Спринт 10 для Yandex.Praktikum - REST API для проекта Yatube

## Описание проекта

Проект представляет собой REST API для проекта Yatube - социальной сети для публикации личных дневников.

Более подробно описание проекта Yatube представлено в https://github.com/pavel-sudomoin/hw05_final#readme

В данном API реализован следующий функционал:
* Авторизация по JWT (JSON Web Token) токену
* Просмотр, создание, удаление и изменение записей (публикаций)
* Просмотр, создание, удаление и изменение комментариев
* Просмотр и создание групп
* Подписка на пользователя

API разработано в учебных целях для **Yandex.Praktikum**.

## Используемые технологии

* Django 2.2
* Python 3.8
* Django Rest Framework
* ReDoc

## Установка проекта

Клонируйте данный репозиторий на свой компьютер и перейдите в папку проекта.
<pre><code>git clone https://github.com/pavel-sudomoin/api_final_yatube</code>
<code>cd api_final_yatube</code></pre>

Создайте и активируйте виртуальное окружение:

<pre><code>python -m venv venv</code>
<code>source ./venv/Scripts/activate  #для Windows</code>
<code>source ./venv/bin/activate      #для Linux и macOS</code></pre>

Установите требуемые зависимости:

<pre><code>pip install -r requirements.txt</code></pre>

Примените миграции:

<pre><code>python manage.py migrate</code></pre>

Запустите django-сервер:

<pre><code>python manage.py runserver</code></pre>

## Документирование API

Структура запросов и ответов API документирована в ReDoc.

После запуска проекта документация доступна по адресу http://localhost:8000/redoc/

## Примеры запросов

* ### Получение токена авторизации
    **Request**
    ```
        POST /api/v1/token/
        body: {"username": "string", "password": "string"}
    ```
    **Response**
    ```
        {
          "refresh": "<JRW-refresh-token>",
          "access": "<JRW-access-token>",
        }
    ```

* ### Обновление токена
    **Request**
    ```
        POST /api/v1/token/refresh/
        body: {"refresh": "JRW-refresh-token"}
    ```
    **Response**
    ```
        {
          "access": "<new-JRW-access-token>"
        }
    ```

* ### Получение списка всех публикаций
    **Request**
    ```
        GET /api/v1/posts/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        [
            {
                "id": 0,
                "text": "string",
                "author": "string",
                "pub_date": "2019-08-24T14:15:22Z"
            },
            ...
        ]
    ```

* ### Создание новой публикации
    **Request**
    ```
        POST /api/v1/posts/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": 0,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Получение публикации по её id
    **Request**
    ```
        GET /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <post_id>,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Обновление публикации по её id
    #### Request
    ```
        PUT /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "new_string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <post_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Частичное обновление публикации по её id
    **Request**
    ```
        PATCH /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "new_string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <post_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Удаление публикации по её id
    **Request**
    ```
        DELETE /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "new_string"}
    ```
    **Response**
    ```
        status_code: 204
    ```

* ### Получение списка всех комментариев
    #### Request
    ```
        GET /api/v1/posts/{post_id}/comments/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        [
            {
                "id": 0,
                "text": "string",
                "author": "string",
                "pub_date": "2019-08-24T14:15:22Z"
            },
            ...
        ]
    ```

* ### Создание нового комментария
    **Request**
    ```
        POST /api/v1/posts/{post_id}/comments/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": 0,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Получение комментария по его id
    **Request**
    ```
        POST /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <comment_id>,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Обновление комментария по его id
    #### Request
    ```
        PUT /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text: "new_string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <comment_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Частичное обновление комментария по его id
    **Request**
    ```
        PATCH /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text: "new_string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <comment_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }

* ### Удаление комментария по его id
    #### Request
    ```
        DELETE /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 204
    ```

* ### Получение списка всех подписчиков
    **Request**
    ```
        GET /api/v1/follow/?search={username_string}
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        [
            {
                "user": "string",
                "following": "string"
            },
            ...
        ]
    ```

* ### Создание подписки
    **Request**
    ```
        POST /api/v1/follow/?user={username_string}
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"following": "string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "user": "string",
            "following": "string"
        }
    ```

* ### Получение списка всех групп
    **Request**
    ```
        GET /api/v1/follow/group/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        [
            {
                "title": "string"
            },
            ...
        ]
    ```

* ### Создание новой группы
    **Request**
    ```
        POST /api/v1/follow/group/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"title": "string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "title": "string"
        }
    ```

## Авторы

* [Yandex.Praktikum](https://praktikum.yandex.ru/)

* [Судомоин Павел](https://github.com/pavel-sudomoin/)
