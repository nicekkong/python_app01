from django.db import models

# Create your models here.
from django.utils import timezone


class MyNumbers(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    create_date = models.DateTimeField()

    def __str__(self):
        return "%s | lv.%s" % (self.name, self.level)

    def setCreateDate(self):
        print(timezone.now())
        self.create_date = timezone.now()
        print("Call setCreateDate()~!!")
        self.save()