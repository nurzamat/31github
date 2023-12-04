from django.db import models
from django.contrib.auth.models import User
from imagekit import ImageSpec
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit, Adjust
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    password_hash = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=40, null=True)
    api_key = models.CharField(max_length=50, null=True)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    gcm_registration_id = models.TextField
    displayed_name = models.CharField(max_length=60, default='', blank=True)
    avatar_original_image = ProcessedImageField(upload_to='avatars',
                                                default='',
                                                processors=[ResizeToFit(480, 480)],
                                                format='JPEG',
                                                blank=True,
                                                options={'quality': 75})
    profile_image = ProcessedImageField(upload_to='profile',
                                        default='',
                                        processors=[ResizeToFill(300, 300)],
                                        format='JPEG',
                                        blank=True,
                                        options={'quality': 60})

    def avatar_30(self):
        if self.avatar_original_image:
            avatar = Thumbnail(source=self.avatar_original_image)
            return '/media/' + avatar.cachefile_name
        else:
            #set 10px less size since 5px padding. See settings for PYDENTICON_PADDING
            return identicon_url(self.user.username, '30')

    def __str__(self):
        return self.user.username


def identicon_url(source, size):
        return '/identicon/image/' + source + '.png?w=' + size + '&h=' + size


class Thumbnail(ImageSpec):
    processors = [ResizeToFill(30, 30), Adjust(contrast=1.2, sharpness=1.1)]
    format = 'JPEG'
    options = {'quality': 80}