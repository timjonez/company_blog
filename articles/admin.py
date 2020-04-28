from django.contrib import admin
from .models import Article, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
