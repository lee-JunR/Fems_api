from django.contrib import admin
from django.urls import path, include
from .views import addFemsTransData,addFemsPayload

urlpatterns = [
    path('temp/monitor/', addFemsTransData.as_view()),
    path('test/monitor/',addFemsPayload.as_view()),
]
