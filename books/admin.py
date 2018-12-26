from django.contrib import admin

from .models import Author, Pubilsh, Classification, Tag, Book

admin.site.register(Author)
admin.site.register(Pubilsh)
admin.site.register(Classification)
admin.site.register(Tag)
admin.site.register(Book)
# Register your models here.
