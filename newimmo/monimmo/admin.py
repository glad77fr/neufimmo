from django.contrib import admin
from .models import Promoteur
from .models import Programme
from .models import Post
from .models import Subject

class PromoteurAdmin(admin.ModelAdmin):
    list_filter = ('nom',)
    list_display = ('nom',)

class ProgrammeAdmin(admin.ModelAdmin) :
    list_filter = ('nom',)
    list_display = ('nom',)

class PostAdmin(admin.ModelAdmin) :
    list_filter = ('post_at',)
    list_display = ('post_at',)

class SubjectAdmin(admin.ModelAdmin) :
    list_display = ('title',)
    readonly_fields = ('post_at',)

admin.site.register(Promoteur, PromoteurAdmin)
admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Subject, SubjectAdmin)

# Register your models here.
