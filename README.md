# Спринт 10 для Yandex.Praktikum - REST API для проекта Yatube

## Описание проекта

Проект представляет собой REST API для проекта Yatube - социальной сети для публикации личных дневников.

Более подробно описание проекта Yatube представлено в https://github.com/pavel-sudomoin/hw05_final#readme

В данном API реализован следующий функционал:
* Авторизация по JWT (JSON Web Token) токену
* Просмотр, создание, удаление и изменение записей
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

## Авторы

* [Yandex.Praktikum](https://praktikum.yandex.ru/)

* [Судомоин Павел](https://github.com/pavel-sudomoin/)
