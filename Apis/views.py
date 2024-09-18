from rest_framework import generics

from Books.models import Book
from .serializers import BookSerializer 

class BookAPLView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
