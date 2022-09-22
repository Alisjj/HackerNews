from rest_framework import serializers

from newsList.models import Item

class ItemSerializer(serializers.ModelSerializer):

    by = serializers.SerializerMethodField(source='get_by')
    def get_by(self, item):
        by = item.by
        return by

    class Meta:
        model = Item
        fields = (
            'id',
            'by',
            'type',
            'time',
            'text',
            'title',
            'url',
            'parent',
        )