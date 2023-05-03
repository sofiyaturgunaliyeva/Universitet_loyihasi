from django.http import HttpResponse
from django.shortcuts import render
from.models import *
from django.shortcuts import redirect


def salomlash(sorov):
    return HttpResponse("Salom dunyo")

# vazifa
# 5 Universitet loyihasida biron fanni o’chirib yuboruvchi view yozing.
def fan_ochir(sorov,son):
    Fan.objects.filter(id = son).delete()
    return redirect('/barcha_fanlar/')


# 6-topshiriq Biron yo’nalishni o’chirib yuboruvchi view yozing.

def barcha_yonalish(sorov):
    soz = sorov.GET.get('qidiruv')
    if soz == "" or soz is None:
        content = {
            "yonalishlar": Yonalish.objects.all()
        }
    else:
        content = {
            "yonalishlar": Yonalish.objects.filter(nom__contains = soz)
        }
    return render(sorov, 'barcha_yonalishlar.html',content)

def yonalish_ochirish(sorov,son):
    Yonalish.objects.filter(id = son).delete()
    return redirect('/barcha_yonalish/')


# 7-topshiriq 7. Fanni nomi bo’yicha qidirish imkoniyatini qo’shing.
def barcha_fanlar(sorov):
    soz = sorov.GET.get('qidiruv')
    if soz == "" or soz is None:
        content = {
            "fanlar": Fan.objects.all()
        }
    else:
        content = {
            "fanlar": Fan.objects.filter(nom__contains = soz)
        }
    return render(sorov, 'barcha_fanlar.html',content)


# 8- topshiriq Ustozni ismi bo’yicha qidirish imkoniyatini qo’shing.

def barcha_ustozlar(sorov):
    soz = sorov.GET.get('qidiruv')
    if soz == "" or soz is None:
        content = {
            "ustozlar": Ustoz.objects.all()
        }
    else:
        content = {
            "ustozlar": Ustoz.objects.filter(ism__contains = soz)
        }
    return render(sorov, 'barcha_ustozlar.html',content)


# 9-topshiriq Biron ustozni o’chirib yuborish uchun view yozing.

def ustoz_ochirish(sorov,son):
    Ustoz.objects.filter(id = son).delete()
    return redirect('/barcha_ustozlar/')
