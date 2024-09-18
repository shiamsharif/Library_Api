from django.urls import path

from .views import BookAPLView

urlpatterns = [
    path("", BookAPLView.as_view(), name="book_list"),
]
