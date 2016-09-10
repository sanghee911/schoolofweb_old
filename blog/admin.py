# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.contrib import admin
from slugify import slugify
from .models import Post, Category, Tag
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


IS_POPUP_VAR = '_popup'
TO_FIELD_VAR = '_to_field'


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'published', 'modified_at', 'get_categories', 'get_tags')
    readonly_fields = ('created_by', 'created_at', 'modified_by', 'modified_at', 'slug',)
    exclude = ('user',)
    save_on_top = True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            # obj.created_at = datetime.now()
            obj.modified_by = request.user
            # obj.modified_at = datetime.now()
            obj.user = request.user
        else:
            obj.modified_by = request.user
            # obj.modified_at = datetime.now()

        obj.slug = slugify(obj.title)

        obj.save()

    @staticmethod
    def get_categories(obj):
        return "\n".join([category.title for category in obj.category.all()])

    @staticmethod
    def get_tags(obj):
        return ", ".join([tag.title for tag in obj.tag.all()])


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
