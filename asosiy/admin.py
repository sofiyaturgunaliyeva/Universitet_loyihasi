from django.contrib import admin

from.models import *


# 5.  Universitet loyihasidagi Ustozni admin paneldan ismi bo’yicha qidirish imkoniyatini qo’shing.
@admin.register(Ustoz)
class UstozAdmin(admin.ModelAdmin):
    search_fields = ("ism",)


# 6.  Yo’nalishni qayta registratsiya qiling.
# Aktivligi bo’yicha filterlash, nomi bo’yicha qidirish imkoniyatlari bo’lsin.
@admin.register(Yonalish)
class YonalishAdmin(admin.ModelAdmin):
    search_fields = ("nom",)
    list_filter = ("aktiv",)


# 7.  Fanni asosiyligiga, yo’nalishiga qarab filterlash, nomi bo’yicha qidirish imkoniyatlari bo’lsin.

@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    list_display = ("nom","yonalish")
    search_fields = ("nom",)
    list_filter = ("asosiy","yonalish__nom")
    autocomplete_fields = ("yonalish", )




# admin.site.register(Yonalish)

# admin.site.register(Fan)

# admin.site.register(Ustoz)

