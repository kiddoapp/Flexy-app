
from django.urls import path
from users.views import Indexview

urlpatterns = [
    path('home/', Indexview.as_view(), name = 'index'),

]