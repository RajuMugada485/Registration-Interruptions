from django.urls import path
from .views import hello,ability,pre
urlpatterns=[
    path('hello/',hello,name='hello'),
    path('ability/',ability,name='ability'),
    path('pre/',pre,name='pre'),
]