#Описание проекта «Kittens Exhibition»

Проект Kittens это онлайн выставка котят.

#Стек использованных технологий

Python3
Django Framework
Django Rest Framework
SQLite3
DRF-Spectacular
Poetry
#Как запустить проект

##Клонировать репозиторий и перейти в него в командной строке

`git clone git@github.com:Alexey-Koltsov/kittens_exhibition.git`
`cd kittens_exhibition`

##Установить poetry

`pip install poetry`

##Инициировать виртуальное окружение

`poetry config virtualenvs.in-project true`

##Установить зависимости из файла pyproject.toml

`cd backend`
`poetry install`

##Активировать виртуальное окружения

`poetry shell`

##Выполнить миграции

Windows

`python manage.py makemigrations`
`python manage.py migrate`

LinuxmacOS

`python3 manage.py makemigrations`
`python3 manage.py migrate`

#База данных

Тестировать пустой проект неудобно, а наполнять его руками — долго.
Выполните команду для заполенения базы данных тестовыми пользователями и их котиками.

`python manage.py loaddata db.json`

##Запустить проект

Windows

`python manage.py runserver`

LinuxmacOS

`python3 manage.py runserver`

##Эндпоинты

По адресу находятся все эндпоинты проекта

`http://127.0.0.1:8000/api/swagger/`

##Данные для авторизации тестовых пользователей
`
{
  "username": "Alexey",
  "password": "nastroenie"
}
`
`
{
  "username": "vanusha",
  "password": "superpuper"
}
`
`
{
  "username": "nastena",
  "password": "devochka"
}
`

#Автор: Кольцов Алексей.