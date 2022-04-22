import os
from collections import Counter
from datetime import datetime
from typing import List

import pdfkit
import qrcode
from django.conf import settings
from jinja2 import Environment, FileSystemLoader

from .models import Item

TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(settings.BASE_DIR, 'templates')),
    trim_blocks=False)
PDFKIT_CONFIG = pdfkit.configuration(
    wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')


def render_template(template_filename: str, context: dict):
    """Генерация шаблона для чека"""
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_receipt_html(items_id: List[int], items) -> None:
    """
    Создание контекста для функции render_template.
    Сохранение файла last_generated_cheque.html в директории media
    """
    fname = 'last_generated_cheque.html'
    c = Counter(items_id)
    # items = Item.objects.filter(id__in=items_id)
    total_price = 0
    for item in items:
        item.quantity = c[item.id]
        item.total_item_price = item.price * item.quantity
        total_price += item.total_item_price
    context = {
        'items': items,
        'total_price': total_price,
        'date': datetime.today().strftime('%d.%m.%Y %H:%M')
    }
    with open(f'media/{fname}', 'wb') as f:
        html = render_template('test.html', context)
        f.write(html.encode('utf-8'))


def create_pdf_from_html(unique_id: str) -> None:
    """
    Преобразует html в pdf
    Путь к pdf файлу: /media/pdf_cheque/{unique_id}.pdf
    """
    pdfkit.from_file('media/last_generated_cheque.html',
                     f'media/pdf_cheque/{unique_id}.pdf',
                     configuration=PDFKIT_CONFIG)


def create_qrcode(server_scheme: str, server_host: str, unique_id: str) -> str:
    """
    Создание QR-кода, содержащего ссылку на чек
    Путь к png файлу QR-кода: /media/qrcode/qrcode_{unique_id}.pdf
    Возвращает ссылку на QR-код
    """
    input_data = f'{server_scheme}://{server_host}/media/pdf_cheque/{unique_id}.pdf'
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(os.path.join(settings.BASE_DIR, 'media',
                          'qrcode', f'qrcode_{unique_id}.png'))
    qrcode_url = f'{server_scheme}://{server_host}/media/qrcode/qrcode_{unique_id}.png'
    return qrcode_url
