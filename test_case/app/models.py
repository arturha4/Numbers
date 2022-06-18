import datetime

from django.db import models


class Course(models.Model):
    date=models.DateTimeField(default=datetime.date.today())
