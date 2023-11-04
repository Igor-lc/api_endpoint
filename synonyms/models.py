from django.db import models

class Synonyms(models.Model):
    eng_synonyms = models.TextField()
    ukr_synonyms = models.TextField()

