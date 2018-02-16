from django.contrib import admin

from .models import Gallery, Photo

from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin


class MyModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
    list_display = ('titolo_galleria', 'slug', 'id', 'Gallery_Thumb', 'created_date_gallery', 'published_date', 'author')
    search_fields = ('titolo_galleria', 'id',)
    list_filter = ('published_date', 'author')
    prepopulated_fields = {"slug": ("titolo_galleria",)}



class ProjectPhoto(admin.ModelAdmin):
    list_display = ('titolo_photo', 'id', 'gallery', 'Upload_photo', 'created_date', 'published_date', 'author')
    search_fields = ('titolo_photo', 'id',)
    list_filter = ('published_date', 'author')

# Register your models here.
admin.site.register(Gallery, MyModelAdmin)
admin.site.register(Photo, ProjectPhoto)
