from django.contrib import admin

from .models import Category, KouryakuPost

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')
  list_display_links = ('id', 'title')
admin.site.register(Category, CategoryAdmin)

class KouryakuPostAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')
  list_display_links = ('id', 'title')
admin.site.register(KouryakuPost, KouryakuPostAdmin)

# Register your models here.
