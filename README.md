
# 💱 Currency API 💱


## Описание

 Проект выполнен в качестве тестового задания для [Kokoc Group](https://kokocgroup.ru/).
 Отображает курс валюты по отношению к рублю на заданную дату. Например, при обращении к приложению по
адресу http://localhost:8000/rate/?charcode=AUD&date=2024-01-01 , оно выводит результат в виде JSON в формате:
```json
{
"charcode": "AUD",
"date": "2024-01-01",
"rate": 57.0627
}
```
Данные по валютам хранятся в базе данных приложения.
Приложение автоматически раз в сутки опрашивает API ЦБ РФ и подгружает актуальные данные в БД.

## Стэк технологий

- Django.
- PostgreSQL в качестве базы данных.
- [Django-crontab](https://pypi.org/project/django-crontab/) для реализации выполнения фоновых задач в указанное время.
- [Requests](https://requests.readthedocs.io/en/latest/) для доступа к API Центробанка РФ.
- Docker.

## Установка

Склонируйте репозиторий:
```bash
git clone https://github.com/blakkheart/currency_test_task.git
```
Перейдите в директорию проекта:
```bash
cd currency_test_task
```
Установите необходимые зависимости:
```bash
pip install -r requirements.txt
```


## Использование  

Введите команду для запуска докер-контейнера:
```bash
docker compose up
```
Создайте и запустите миграции и запустите планировщик задач:
```bash
docker compose exec backend python manage.py makemigrations
docker compose exec backend python manage.py migrate
docker compose exec backend python crontab add
``` 
Если все сделано корректно, сервер запустится по адресу localhost:8000/rate/ и вы сможете получить доступ к API.


### Дополнительно
Вы можете поменять время опроса API ЦБ РФ, изменив значение в переменной *CRONJOBS* в файле *settings.py*, или, если есть необходимость, опрашивать можно вручную с помощью команды: 
```bash
python manage.py load_data
```
Также вы можете создать суперпользователя
```bash
python manage.py createsuperuser
```
и изменять значения через админ-панель по адресу localhost:8000/admin/