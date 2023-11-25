from decimal import Decimal

from django.contrib.auth.models import User



class UserDetails():
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=60, null=True)
    phone = models.CharField(max_length=60, null=True)
    city = models.CharField(max_length=60, null=True)
    country = models.CharField(max_length=60, null=True)
    address = models.CharField(max_length=60, null=True)
    class Meta:
        verbose_name_plural = "User details"

    def __str__(self):
        return self.user.username + get_status(self.status)