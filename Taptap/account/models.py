from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=60, null=True)
    phone = models.CharField(max_length=60, null=True)
    city = models.CharField(max_length=60, null=True)
    country = models.CharField(max_length=60, null=True)
    address = models.CharField(max_length=60, null=True)
    status = models.IntegerField(default=0, null=True)
    created_date = models.DateTimeField(auto_now=False, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.user.username