# Инструкция по запуску
1. **Склонируйте репозиторий**

```
git clone https://github.com/dyachkov-pavel/cash_register.git
```

2. **Перейдите в директорию cash_register**

```
cd cash_register
```

3. **Создайте и активируйте виртуальное окружение**

```
python -m venv venv
```

```
source venv/Scripts/activate
```

4. **Установите зависимости**

```
pip install -r requirements.txt
```

5. **Миграции**

```
python manage.py makemigrations items
```

```
python manage.py migrate
```

6. **Создайте супер юзера**

```
winpty python manage.py createsuperuser
```

7. **Запустите сервер**

```
python manage.py runserver
```
8. **Возможно для правильной работы сервера надо будет скачать wkhtmltopdf**\
https://wkhtmltopdf.org/downloads.html \
Затем в файле utils.py указать свой путь установки в перемнной PDFKIT_CONFIG


### Примечание 
Qr-код сохраняется по адресу **/media/qrcode/qrcode_{unique_id}.png** \
Pdf файл сохраняется по адресу **/media/pdf_cheque/{unique_id}.pdf**
