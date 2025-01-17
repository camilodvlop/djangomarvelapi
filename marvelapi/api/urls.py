from django.urls import path
from .views import MarvelCharactersAPIView

urlpatterns = [
     
    path('get-characters/', MarvelCharactersAPIView.as_view(), name='get-characters'),
]