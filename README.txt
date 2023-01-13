REST-сервис для хранения бинарных данных на облачном сервисе S3


Для запуска:

Клонируйте репозиторий
```java
git clone https://github.com/s4dd666/binarydatas3.git
```
Установите зависимости
```java
pip install -r requirements.txt
```
Запуститe сервер
```java
python -m flask run
```

Приложение:

Метод GET - get_data
```java
 http://127.0.0.1:5000/api/v1/data
```

Метод PUT - put_data
```java
 http://127.0.0.1:5000/api/v1/add-data/<key>/<value>
```
key - ключ 
value - значение
