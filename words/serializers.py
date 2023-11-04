from rest_framework.serializers import ModelSerializer

from words.models import Words


class WordSerializer(ModelSerializer):
    class Meta:
        model = Words
        fields = ['english', 'ukrainian']
