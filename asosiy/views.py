from django.http import HttpResponse
from django.shortcuts import render
from.models import *
from django.shortcuts import redirect
from .forms import *

def salomlash(sorov):
    return HttpResponse("Salom dunyo")

# vazifa
# 5 Universitet loyihasida biron fanni o’chirib yuboruvchi view yozing.
def fan_ochir(sorov,son):
    Fan.objects.filter(id = son).delete()
    return redirect('/barcha_fanlar/')


# 6-topshiriq Biron yo’nalishni o’chirib yuboruvchi view yozing.

def barcha_yonalish(sorov):
    if sorov.method == 'POST':
        f = YonalishForm(sorov.POST)
        if f.is_valid():
            Yonalish.objects.create(
                nom = f.cleaned_data['nom'],
                aktiv=f.cleaned_data['aktivligi']
            )
        return redirect('/barcha_yonalish/')
    soz = sorov.GET.get('qidiruv')
    if soz == "" or soz is None:
        content = {
            "yonalishlar": Yonalish.objects.all(),
            "forma":YonalishForm()
        }
    else:
        content = {
            "yonalishlar": Yonalish.objects.filter(nom__contains = soz),
            "form": YonalishForm()
        }
    return render(sorov, 'barcha_yonalishlar.html',content)

def yonalish_ochirish(sorov,son):
    Yonalish.objects.filter(id = son).delete()
    return redirect('/barcha_yonalish/')


# 7-topshiriq 7. Fanni nomi bo’yicha qidirish imkoniyatini qo’shing.
def barcha_fanlar(sorov):
    if sorov.method == 'POST':
        forma = FanForm(sorov.POST)
        if forma.is_valid():
            forma.save()
        # Fan.objects.create(
        #     nom = sorov.POST.get('n'),
        #     yonalish = Yonalish.objects.get(id=sorov.POST.get('y')),
        #     asosiy = True
        # )
        return redirect('/barcha_fanlar/')
    soz = sorov.GET.get('qidiruv')
    if soz == "" or soz is None:
        content = {
            "fanlar": Fan.objects.all(),
            "yonalishlar": Yonalish.objects.all(),
            "forma": FanForm()
        }
    else:
        content = {
            "fanlar": Fan.objects.filter(nom__contains = soz),
            "yonalishlar": Yonalish.objects.filter(nom__contains = soz),
            "forma": FanForm()
        }
    return render(sorov, 'barcha_fanlar.html',content)


# 8- topshiriq Ustozni ismi bo’yicha qidirish imkoniyatini qo’shing.

def barcha_ustozlar(sorov):
    if sorov.method == 'POST':
        if sorov.method == 'POST':
            forma = UstozForm(sorov.POST)
            if forma.is_valid():
                forma.save()
        # Ustoz.objects.create(
        #     ism=sorov.POST.get('i'),
        #     yosh=sorov.POST.get('y'),
        #     jins=sorov.POST.get('j'),
        #     daraja=sorov.POST.get('d'),
        #     fan=Fan.objects.get(id=sorov.POST.get('f'))
        # )
        return redirect('/barcha_ustozlar/')

    soz = sorov.GET.get('qidiruv')
    if soz == "" or soz is None:
        content = {
            "ustozlar": Ustoz.objects.all(),
            "fanlar": Fan.objects.all(),
            "forma":UstozForm()
        }
    else:
        content = {
            "ustozlar": Ustoz.objects.filter(ism__contains=soz),
            "fanlar": Fan.objects.filter(nom__contains=soz),
            "forma": UstozForm()
        }

    return render(sorov, 'barcha_ustozlar.html', content)


# 9-topshiriq Biron ustozni o’chirib yuborish uchun view yozing.

def ustoz_ochirish(sorov,son):
    Ustoz.objects.filter(id = son).delete()
    return redirect('/barcha_ustozlar/')



# Vazifa
 # 4-topshiriq  Universitet loyihasidagi Fan ma’lumotini o’zgartirish imkoniyatini qo’shing.

def fan_ozgartir(sorov, son):
    if sorov.method == 'POST':
        Fan.objects.filter(id = son).update(
            nom = sorov.POST.get('n'),
            yonalish = Yonalish.objects.get(id = sorov.POST.get('y')),
            asosiy = True
        )
        return redirect('/barcha_fanlar/')
    f = Fan.objects.get(id = son)
    content = {
        "fanlar": f,
        "yonalishlar": Yonalish.objects.exclude(id=f.yonalish.id)
    }
    return render(sorov, 'fan_ozgartir.html', content)


# 5-topshiriq  Yo’nalish ma’lumotini o’zgartirish imkoniyatini qo’shing.

def yonalish_ozgartir(sorov, son):
    if sorov.method == 'POST':
        Yonalish.objects.filter(id = son).update(
            nom = sorov.POST.get('n'),
            aktiv = True
        )
        return redirect('/barcha_yonalish/')
    content = {
        "yonalish": Yonalish.objects.get(id = son)
    }
    return render(sorov, 'yonalish_ozgartir.html', content)

# 6-topshiriq  Ustoz ma’lumotini o’zgartirish imkoniyatini qo’shing.

def ustoz_ozgartir(sorov, son):
    if sorov.method == 'POST':
        Ustoz.objects.filter(id = son).update(
            ism = sorov.POST.get('i'),
            yosh =sorov.POST.get('y'),
            jins=sorov.POST.get('j'),
            daraja=sorov.POST.get('d'),
            fan = Fan.objects.get(id = sorov.POST.get('f')),
        )
        return redirect('/barcha_ustozlar/')
    u = Ustoz.objects.get(id = son)
    content = {
        "ustoz": u,
        "fanlar": Fan.objects.exclude(id=u.fan.id)
    }
    return render(sorov, 'ustoz_ozgartir.html', content)
