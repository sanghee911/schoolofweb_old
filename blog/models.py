# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from hitcount.models import HitCount


class PostManager(models.Manager):

    def top_five_posts(self):
        posts = self.get_queryset().all()
        sorted_posts = sorted(posts, key=lambda obj: obj.hitcount(), reverse=True)[:5]
        return sorted_posts


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
    created_at = models.DateTimeField(verbose_name='작성일시', auto_now_add=True)
    modified_by = models.ForeignKey(User, verbose_name='수정자', related_name='modified_by', null=True, blank=True)
    modified_at = models.DateTimeField(verbose_name='수정일시', auto_now=True)
    published = models.CharField(max_length=20, choices=choices, default='draft')
    published_time = models.DateTimeField(verbose_name='공개 일시', blank=True, null=True)
    user = models.ForeignKey(User, related_name='user', null=True, blank=True)

    # initiate PostManager
    objects = PostManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def hitcount(self):
        hitcount_obj = HitCount.objects.get_for_object(self)
        hits = hitcount_obj.hits
        return hits

    def hitcount_by_date(self, **date_dict):
        hitcount_obj = HitCount.objects.get_for_object(self)
        hits_by_date = hitcount_obj.hit_set.all().filter(created__year=date_dict['year'],
                                                         created__month=date_dict['month'],
                                                         created__day=date_dict['day'])
        return hits_by_date.count()

    def get_next(self):
        if not self.published == 'published':
            return None
        new_posts = Post.objects.filter(published='published').filter(published_time__gt=self.published_time)
        if new_posts:
            return new_posts.last()

    def get_previous(self):
        if not self.published == 'published':
            return None
        old_posts = Post.objects.filter(published='published').filter(published_time__lt=self.published_time)
        if old_posts:
            return old_posts.first()


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:category_list', kwargs={'slug': self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:tag_list', kwargs={'slug': self.slug})
