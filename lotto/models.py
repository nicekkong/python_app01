import random

from django.db import models

# Create your models here.
from django.utils import timezone


class GuessNumbers(models.Model):
    name = models.CharField(max_length=24)
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]')
    text = models.CharField(max_length=255)
    num_lotto = models.IntegerField(default=5)
    update_date = models.DateTimeField()

    def __str__(self):
        return "%s %s" % (self.name, self.text)

    # 로또 번호 생성하고 저장
    def generate(self):
        self.lottos = ""
        origin = list(range(1, 46))
        for _ in range(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            print("origin[:6] : ", guess)
            print("before sort() : ", guess)
            guess.sort()
            print("After sort() : ", guess)
            self.lottos += str(guess) + '\n'
        self.update_date = timezone.now()
        self.save()