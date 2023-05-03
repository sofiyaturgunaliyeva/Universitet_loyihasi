from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('barcha_fanlar/',barcha_fanlar),
    path('barcha_yonalish/',barcha_yonalish),
    path('barcha_ustozlar/',barcha_ustozlar),
    path('fan_ochir/<int:son>/',fan_ochir),
    path('yonalish_ochirish/<int:son>/',yonalish_ochirish),
    path('ustoz_ochirish/<int:son>/',ustoz_ochirish),
]
