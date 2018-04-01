# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, to_field='username')
    profile_picture = models.ImageField(blank=True, null=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.user_id

    def save(self, *args, **kwargs):
        #self.full_name = self.user.first_name + ' ' + self.user.last_name
        self.full_name = self.user.last_name + ' ' + self.user.first_name
        super(UserProfile, self).save(*args, **kwargs)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

