from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from words.models import Words
from words.serializers import WordSerializer


def words_page(request):
    return render(request, 'index.html', {'words': Words.objects.all()})


class WordView(ModelViewSet):
    queryset = Words.objects.all()
    serializer_class = WordSerializer

def words_app(request):
    return render(request, 'main_app.html')