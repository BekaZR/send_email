from django.db import models


class SendMail(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} -- {self.date}'
