from django.db import models
from django.contrib.auth.models import User

class Policy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="policies")
    policy_number = models.CharField(max_length=50, unique=True)
    provider = models.CharField(max_length=100)
    policy_type = models.CharField(max_length=255, null=True)
    start_date = models.DateField(null=True)
    expiry_date = models.DateField()
    reminder_date = models.BooleanField(default=True)
    # email_notification = models.BooleanField(default=True)
    # sms_notification = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.policy_number} ({self.user.username})"
