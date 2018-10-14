# -*- coding: utf-8 -*-

from django.db import models

class Info(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.title.encode('utf-8')

