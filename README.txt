REST-сервис для хранения бинарных данных на облачном сервисе S3


Для запуска:

Клонируйте репозиторий:
git clone https://github.com/s4dd666/binary-data-s3.git


Установите зависимости:
pip install -r requirements.txt


Запуститe сервер:
python -m flask run


Приложение:

Метод GET - get_data:
http://127.0.0.1:5000/api/v1/data


Метод PUT - put_data:
http://127.0.0.1:5000/api/v1/add-data/<key>/<value>


key - ключ 
value - значение
