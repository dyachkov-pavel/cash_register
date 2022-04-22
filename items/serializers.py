from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    """Сериализатор id товаров"""
    items = serializers.ListField(child=serializers.IntegerField())

    def to_internal_value(self, data):
        """
        Преобразует str в int.
        Поднимает исключение, если элемент из списка 
        не удается преобразовать в числовое значение 
        или список items является пустым
        """
        if len(data['items']) == 0:
            raise serializers.ValidationError('Send at least 1 item id')
        try:
            data['items'] = [int(i) for i in data['items']]
            return data
        except:
            raise serializers.ValidationError('Send valid items ids')
