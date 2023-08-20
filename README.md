# Проект «API для Yatube

## Описание проекта

Проект представляет собой REST API для проекта Yatube - социальной сети для публикации личных дневников.


В данном API реализован следующий функционал:
* Авторизация по JWT (JSON Web Token) токену
* Просмотр, создание, удаление и изменение записей (публикаций)
* Просмотр, создание, удаление и изменение комментариев
* Просмотр и создание групп
* Просмотр подписок и возмодность подписаться на пользователя


## Используемые технологии

* Django 3.2.16
* Python 3.9
* Django Rest Framework
* JWT + Djoser
* ReDoc

## Установка проекта

Клонировать репозиторий и перейти в него в командной строке.

Создайте и активируйте виртуальное окружение:

```bash
   python -m venv venv</code>
   source ./venv/Scripts/activate
```

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
        POST /api/v1/jwt/
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
        POST /api/v1/jwt/refresh/
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
         {
           "count": 123,
           "next": "http://api.example.org/accounts/?offset=400&limit=100",
           "previous": "http://api.example.org/accounts/?offset=200&limit=100",
           "results": [
             {
               "id": 0,
               "author": "string",
               "text": "string",
               "pub_date": "2021-10-14T20:41:29.648Z",
               "image": "string",
               "group": 0
             }
           ]
         }
    ```

* ### Создание новой публикации
    **Request**
    ```
        POST /api/v1/posts/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {
                 "text": "string",
                 "image": "string",
                 "group": 0
             }
    ```
    **Response**
    ```
         {
           "id": 0,
           "author": "string",
           "text": "string",
           "pub_date": "2019-08-24T14:15:22Z",
           "image": "string",
           "group": 0
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
         {
           "id": 0,
           "author": "string",
           "text": "string",
           "pub_date": "2019-08-24T14:15:22Z",
           "image": "string",
           "group": 0
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
         {
           "id": 0,
           "author": "string",
           "text": "string",
           "pub_date": "2019-08-24T14:15:22Z",
           "image": "string",
           "group": 0
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
         {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2019-08-24T14:15:22Z",
            "image": "string",
            "group": 0
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

## Автор

* Демин Матвей
