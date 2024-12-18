from django.db import models
from django.contrib.auth.models import User, AbstractUser


# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     date_of_birth = models.DateTimeField(null=True)
#     profile_picture = models.ImageField(default="default.png", upload_to='profile_pics')
#     phone_number = models.BigIntegerField(null=True)
#     address = models.CharField(max_length=255, null=True)
#     city = models.CharField(max_length=100, null=True)
#     state = models.CharField(max_length=100, null=True)
#     country = models.CharField(max_length=50, null=True)
#     ip_address = models.GenericIPAddressField(unpack_ipv4=True, null=True)

#     def save(self, *args, **kwargs):
#         if not self.username:
#             self.username = f"users_{User.objects.count() + 1}"
#         super().save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username
