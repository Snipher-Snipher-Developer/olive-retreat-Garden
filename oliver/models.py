from django.db import models

class Client(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    Decoration = models.TextField(max_length=200, null=True, blank=True)
    date_booked = models.DateField()
    Date_submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return self.username


