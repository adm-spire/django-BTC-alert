# myapp/models.py

from django.db import models
from django.contrib.auth.models import User

class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_price = models.DecimalField(max_digits=20, decimal_places=8)
    statement = models.CharField(max_length=50)  # Use this field to store triggered status
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Alert {self.id} for user {self.user.username}'

