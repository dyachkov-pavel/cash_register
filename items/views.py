import uuid

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ItemSerializer
from .utils import create_pdf_from_html, create_qrcode, create_receipt_html


@api_view(['POST'])
def generate_cheque(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        ids = request.data.get('items')
        unique_id = str(uuid.uuid4())[:8]
        create_receipt_html(ids)
        create_pdf_from_html(unique_id)
        qrcode_url = create_qrcode(request.scheme,
                                   request.headers["Host"],
                                   unique_id)
        return Response({'qrcode': qrcode_url})
    return Response({'error': 'provide valid ids or send at least 1 item'})
