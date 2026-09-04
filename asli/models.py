from django.db import models

# Create your models here.
class to_do(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    DAYS = [
        ("sat", "شنبه"),
        ("sun", "یکشنبه"),
        ("mon", "دوشنبه"),
        ("tue", "سه‌شنبه"),
        ("wed", "چهارشنبه"),
        ("thu", "پنجشنبه"),
        ("fri", "جمعه"),
    ]
    day=models.CharField(max_length=3,choices=DAYS)

    def __str__(self):
        return self.title