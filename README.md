Whoosh Neural Core
Описание проекта
http://new-ai-education.online/
Whoosh Neural Core — микросервис для управления парком электросамокатов, разработанный на FastAPI с использованием PostgreSQL и Docker.

Проект предоставляет REST API для выполнения базовых операций над самокатами (CRUD), а также автоматически генерирует документацию API через Swagger.

Используемые технологии
Python 3.12
FastAPI
SQLAlchemy 2.0
PostgreSQL
Docker
Docker Compose
Uvicorn
Pydantic
Назначение директорий
app/main.py

Главная точка входа приложения.

Выполняет:

создание приложения FastAPI;
подключение маршрутов;
создание таблиц базы данных;
регистрацию Swagger.
app/database.py

Отвечает за подключение к PostgreSQL.

Содержит:

SQLAlchemy Engine;
SessionLocal;
Base;
зависимость get_db().
app/models

Содержит модели базы данных.

В проекте реализована модель:

Scooter

Поля:

id
serial_number
latitude
longitude
battery_level
is_available
created_at
app/schemas

Содержит Pydantic-модели.

Используются для:

проверки входящих данных;
формирования ответов API.

Реализованы схемы:

ScooterCreate
ScooterUpdate
ScooterResponse
app/services

Бизнес-логика приложения.

Содержит функции:

получение списка самокатов;
поиск самоката;
создание;
обновление;
удаление.
app/routers

Определяет REST API.

Все запросы пользователя попадают сюда.

Возможности сервиса

Микросервис поддерживает полный CRUD.

Можно:

получить список всех самокатов;
получить информацию об одном самокате;
зарегистрировать новый самокат;
изменить координаты;
изменить заряд батареи;
изменить статус доступности;
удалить самокат.
Структура базы данных

Таблица:
Поле	Тип
id	Integer
serial_number	String
latitude	Float
longitude	Float
battery_level	Integer
is_available	Boolean
created_at	DateTime
