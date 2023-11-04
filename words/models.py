from django.contrib.auth.models import User
from django.db import models

from synonyms.models import Synonyms


class Words(models.Model):
    english = models.TextField(null=True)
    ukrainian = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    synonyms = models.ManyToManyField(Synonyms)