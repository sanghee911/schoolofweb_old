# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.contrib import admin
from slugify import slugify
from .models import Post, Category, Tag
import sys
from django.contrib import admin


reload(sys)
sys.setdefaultencoding('utf-8')


IS_POPUP_VAR = '_popup'
TO_FIELD_VAR = '_to_field'


class PostAdmin(admin.ModelAdmin):

    readonly_fields = ('created_by', 'created_at', 'modified_by', 'modified_at', 'slug',)
    exclude = ('user',)
    save_on_top = True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.created_at = datetime.now()
            obj.modified_by = request.user
            obj.modified_at = datetime.now()
            obj.user = request.user
        else:
            obj.modified_by = request.user
            obj.modified_at = datetime.now()

        obj.slug = slugify(obj.title)

        obj.save()


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):

    readonly_fields = ('slug',)

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.title)

        obj.save()


admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):

    readonly_fields = ('slug',)

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.title)

        obj.save()


admin.site.register(Tag, TagAdmin)