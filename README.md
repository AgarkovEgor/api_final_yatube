# Как запустить проект:
## Клонировать репозиторий и перейти в него в командной строке:
    git clone https://github.com/AgarkovEgor/api_final_yatube
    cd api_final_yatube
## Cоздать и активировать виртуальное окружение:
    python3 -m venv env
    source env/bin/activate
## Установить зависимости из файла requirements.txt:
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
## Выполнить миграции:
    python3 manage.py migrate
## Запустить проект:
    python3 manage.py runserver
# Проект «API для Yatube»
## Опсиание
### API для Yatub представляет собой проект социальной сети в которой реализованы следующие возможности, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.
## Стек технологий
- ### Python 3.11
- ### Django 
- ### DRF
- ### JWT + Djoser
# Как запустить проект:
### Клонировать репозиторий и перейти в него в командной строке:
    git clone https://github.com/AgarkovEgor/api_final_yatube
    cd api_final_yatube
### Cоздать и активировать виртуальное окружение:
    python3 -m venv env
    source env/bin/activate
### Установить зависимости из файла requirements.txt:
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
### Выполнить миграции:
    python3 manage.py migrate
### Запустить проект:
    python3 manage.py runserver
## Пример запросов к API для любого пользователя
### Для неавторизованных пользователей работа с API доступна только в режиме чтения
    GET api/v1/posts/ - получить список всех публикаций.
    При указании параметров limit и offset выдача должна работать с пагинацией
    GET api/v1/posts/{id}/ - получение публикации по id
    GET api/v1/groups/ - получение списка доступных сообществ
    GET api/v1/groups/{id}/ - получение информации о сообществе по id
    GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
    GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
## Пример запросов к API для авторизовнного пользователя
### 1) Создание публикации
    POST /api/v1/posts/
### Передаем в body необходимые данные:
    {
    "text": "text",
    "image": "image",
    "group": 1
    }
### 2) Обновление публикации(Доступно только автору рубликации)
    PUT /api/v1/posts/{id}/
### Передаем в body необходимые данные:
    {
    "text": "new text",
    "image": "new image",
    "group": 2
    }
### 3) Частичное обновление публикации(Доступно только автору рубликации)
    PATCH /api/v1/posts/{id}/
### Передаем в body необходимые данные:
    {
    "text": "new text",
    "image": "image",
    "group": 1
    }
### 4) Удаление публикации(Доступно только автору рубликации)
    DELETE /api/v1/posts/{id}/
### 5) Добавление комментария
    POST /api/v1/posts/{post_id}/comments/
### Передаем в body необходимые данные:
    {
    "text":"comment"
    }
### 5) Обновление комментария (Доступно только автору комментария)
    PUT /api/v1/posts/{post_id}/comments/{id}/
### Передаем в body необходимые данные:
    {
    "text":" new comment"
    }
### 6) Удаление комментария (Доступно только автору комментария)
    DELETE /api/v1/posts/{post_id}/comments/{id}/
### 7) Получение подписок текущего пользователя
    GET /api/v1/follow/
### 8) Подписаться на другого пользователя
    POST /api/v1/follow/
### Передаем в body необходимые данные:
    {
    "following": "username"
    }
### 9) Получение JWT-токена
    POST /api/v1/jwt/create/
### Передаем в body необходимые данные:
    {
    "username":"user",
    "password":"qwerty"
    }
