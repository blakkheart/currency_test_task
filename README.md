
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

- [Django](https://www.djangoproject.com/).
- [PostgreSQL](https://www.postgresql.org/) в качестве базы данных.
- [Django-crontab](https://pypi.org/project/django-crontab/) для реализации выполнения фоновых задач в указанное время.
- [Requests](https://requests.readthedocs.io/en/latest/) для доступа к API Центробанка РФ.
- [Redis](https://redis.io/) для работы Celery.
- [Celery](https://docs.celeryq.dev/en/stable/) для реализации выполнения фоновых задач в указанное время в docker-контейнере.
- [Docker](https://www.docker.com/).

## Установка

1. Склонируйте репозиторий:
```bash
git clone https://github.com/blakkheart/currency_test_task.git
```
2. Перейдите в директорию проекта:
```bash
cd currency_test_task
```
3. Установите и активируйте виртуальное окружение:
   - Windows
   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```
   - Linux/macOS
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Обновите [pip](https://pip.pypa.io/en/stable/):
   - Windows
   ```bash
   (venv) python -m pip install --upgrade pip
   ```
   - Linux/macOS
   ```bash
   (venv) python3 -m pip install --upgrade pip
   ```
5. Установите зависимости из файла requirements.txt:
   ```bash
   (venv) pip install -r currency_rate/requirements.txt
   ```
Создайте и заполните файл *.env* по примеру с файлом *.env.example*, который находится в корневой директории.



## Использование  

 - ### Использование с docker:

	1. Введите команду для запуска докер-контейнера:
	```bash
	docker compose up
	```
	2. Создайте и запустите миграции:
	```bash
	docker compose exec backend python manage.py makemigrations
	docker compose exec backend python manage.py migrate
	``` 
	3. Соберите и скопируйте статику:
	```bash
	docker compose exec backend python manage.py collectstatic
	docker compose exec backend cp -r /currency_app/collected_static/. /backend_static/static/
	```
	
- ### Использование без docker:
	1. Перейдите в папку с файлом manage.py:
	```bash
	cd currency_rate
	```
	2. Создайте и запустите миграции:
	```bash
	(venv) python manage.py makemigrations
	(venv) python manage.py migrate
	```
	3. Запустите планировщик задач:
	```bash
	(venv) python manage.py crontab add 
	```
	Вы можете проверить, что планировщик работает и удалить его в случае необходимости с помощью команд:
	```bash
	(venv) python manage.py crontab show
	(venv) python manage.py crontab remove
	```
	4. Запустите сервер:
	```bash
	(venv) python manage.py runserver
	```
Если все сделано корректно, сервер запустится по адресу localhost:8000 и вы сможете получить доступ к API.
Доступны два эндпоинта - localhost:8000/rate/?charcode={ВАЛЮТА}&date={ДАТА} и localhost:8000/admin/

### Дополнительно
Вы можете поменять время опроса API ЦБ РФ, изменив значение в переменной *CRONJOBS* в файле *settings.py*, если запускается без docker, или значение переменной *CELERY_BEAT_SCHEDULE.schedule*, если запускается через docker, или, если есть необходимость, опрашивать можно вручную с помощью команды: 
```bash
python manage.py load_data
```
Также вы можете создать суперпользователя и изменять значения через админ-панель по адресу localhost:8000/admin/ :
```bash
python manage.py createsuperuser
```
