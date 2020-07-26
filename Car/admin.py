from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class CarAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Car
        fields = '__all__'


class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("model",)}
    form = CarAdminForm
    list_display = ('id', 'manufacturer', 'model', 'content', 'gear_box', 'get_photo',)
    list_display_links = ('id', 'model',)
    search_fields = ('model',)
    list_filter = ('manufacturer',)
    readonly_fields = ('get_photo',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50"')
        return '-'

    get_photo.short_description = 'Фото'


class ManufacturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
