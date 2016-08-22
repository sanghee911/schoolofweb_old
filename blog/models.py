# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from hitcount.models import HitCount


class Post(models.Model):

    class Meta:
        ordering = ['-published_time']

    choices = [('published', 'published'), ('draft', 'draft')]

    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    content = RichTextUploadingField(verbose_name='내용', null=True, blank=True)
    category = models.ManyToManyField('Category', related_name='category_post', blank=True)
    tag = models.ManyToManyField('Tag', related_name='tag_post', blank=True)
    thumbnail = models.ImageField(upload_to='thumbnail/')
    created_by = models.ForeignKey(User, verbose_name='작성자', related_name='created_by', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='작성일시', blank=True, null=True)
    modified_by = models.ForeignKey(User, verbose_name='수정자', related_name='modified_by', null=True, blank=True)
    modified_at = models.DateTimeField(verbose_name='수정일시', blank=True, null=True)
    published = models.CharField(max_length=20, choices=choices, default='draft')
    published_time = models.DateTimeField(verbose_name='공개 일시', blank=True, null=True)
    user = models.ForeignKey(User, related_name='user', null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def hitcount(self):
        hitcount_obj = HitCount.objects.get_for_object(self)
        hits = hitcount_obj.hits
        return hits


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'slug': self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:tag_detail', kwargs={'slug': self.slug})