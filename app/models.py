from django.db import models


# Create your models here.
class duplicate(models.Model):
    ok = models.BooleanField(default='')


class user(models.Model):
    members = models.ForeignKey(duplicate, on_delete=models.CASCADE, default='', related_name='member')
    id = models.CharField(max_length=10, primary_key=True)
    real_name = models.CharField(max_length=70)
    tz = models.CharField(max_length=80)

    def __str__(self):
        return self.real_name


class activity(models.Model):
    user_activity = models.ForeignKey(user, related_name='activity_periods', on_delete=models.CASCADE)
    start_time = models.DateTimeField(default='')
    end_time = models.DateTimeField(default='')
