from django.contrib import admin
from .models import Promoteur, Programme, Post, Subject, Topic, Reservation, Building

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

class TopicAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def get_queryset(self, request):
        queryset = super(TopicAdmin, self).get_queryset(request)
        queryset = queryset.order_by('subject')
        return queryset

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('programme', 'user',)

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('programme', 'building_name',)

admin.site.register(Promoteur, PromoteurAdmin)
admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Building, BuildingAdmin)
# Register your models here.
