# Тестовое задание: Backend

Этот репозиторий содержит решение тестового задания Backend для [Bolid](https://observant-resistance-a1d.notion.site/Backend-fefe433815854ea4829bef60dca4228b).

## Описание

В данном проекте реализовано решение тестового задания Backend для Bolid. Решение включает в себя следующие основные компоненты:

- **API**: Реализация API с использованием FastAPI для работы с событиями и датчиками.
- **База данных**: Инициализация и миграции базы данных с использованием SQLAlchemy и Alembic.
- **Модели данных**: Определение моделей данных для событий и датчиков.
- **CRUD операции**: Реализация операций создания, чтения, обновления и удаления (CRUD) для событий и датчиков.

## Структура проекта

Test_Bolid/  
│  
├── app/  
│ ├── init.py  
│ ├── crud.py  
│ ├── database.py  
│ ├── main.py  
│ ├── models/  
│ │ ├── init.py  
│ │ ├── event.py  
│ │ └── sensor.py  
│ ├── routers/  
│ │ ├── init.py  
│ │ ├── events.py  
│ │ └── sensors.py  
│ └── schemas/  
│ ├── init.py  
│ ├── event.py  
│ └── sensor.py  
│  
├── alembic/  
│ ├── versions/  
│ │ └── ...  
│ ├── env.py  
│ ├── README  
│ └── script.py.mako  
│  
├── .env  
├── .gitignore  
├── alembic.ini  
├── Dockerfile  
├── README.md  
└── requirements.txt  

## Требования

- Docker
- Docker Compose

## Установка и запуск на локальном сервере

1. Клонировать репозиторий:

    ```bash
    git clone https://github.com/SharkDeveloper/Test_Bolid.git
    cd Test_Bolid
    ```
2. В файле .env установить свои переменные окружения(рекомендуется не использовать предустанволенные):

    ```bash
    POSTGRES_USER=...
    POSTGRES_PASSWORD=...
    POSTGRES_DB=...
    ```

3. Запустить Docker Compose:

    ```bash
    docker-compose up --build
    ```
4. Для проверки, что все работает корректно ,запустить в бразуере страницу по адресу:

    ```bash
    http://localhost:8000/
    ```

## Дополнительная информация

1. Нумерация ID событий и датчиков начинается с 1.
2. При необходимости загрузить события из файла, необходимо запустить ф-цию load_events_from_json из файла /app/utils.py в функциии get_db файла /app/routers/events.py
