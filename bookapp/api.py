from rest_framework.viewsets import ModelViewSet
from .serializers import MusicSerializer
from .models import Book


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = MusicSerializer

