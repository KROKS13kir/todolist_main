Курсовая работа № 6 - Todolist

Описание
    
    Приложение для постановки целей

Stack
    
    backend - django
    database - postgresql
    version - python3.8

Launch (порядок действий)

    установить зависимости - pip install -r requirements.txt
    запустить базу - docker-compose up --build -d
    заполнить .env значениями
    накатить миграции - python manage.py migrate
    запустить проект - python manage.py runserver