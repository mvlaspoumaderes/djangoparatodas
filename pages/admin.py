from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_disply = ('title', 'update_date')
    ordering = ('title',)
    seach_fields = ('title',)

admin.site.register(Page, PageAdmin)


