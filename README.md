# Устанавливаем виртуалку
# Linux
python3 -m venv env
или
# Windows
python -m venv env

# Запускаем виртуалку
# Linux
source env/bin/activate
# Windows
env\Scripts\activate 

# Установливаем пакеты
pip install -r requirements.txt

# Создаем базу и заполняем файл .env  следующим содержимым:
DEBUG=''
SECRET_KEY=''
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
DB_PORT=''

# Миграции в базу
python manage.py migrate

# Запуск
python manage.py runserver

# Создаем админа
python manage.py createsuperuser