from django.contrib import admin

# Register your models here.
from .models import Blog
admin.site.register(Blog)
#class ArticleModel(admin.ModelAdmin):
    #list_filter = ('title','description','date','time')
    #list_display =('title','description','date','time')
    #date_hierarchy =('date')
   