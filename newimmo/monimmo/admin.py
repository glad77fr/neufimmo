from django.contrib import admin
from .models import Promoteur
from .models import Programme

class PromoteurAdmin(admin.ModelAdmin):
    list_filter = ('nom',)
    list_display = ('nom',)

class ProgrammeAdmin(admin.ModelAdmin) :
    list_filter = ('nom',)
    list_display = ('nom',)

admin.site.register(Promoteur, PromoteurAdmin)
admin.site.register(Programme, ProgrammeAdmin)

# Register your models here.
