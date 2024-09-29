from django.db import models

class Phrase(models.Model):
    phrase_en = models.CharField('phrase_en',max_length=300, unique=True)
    phrase_ru = models.CharField('phrase_ru',max_length=300, unique=True)

    def __str__(self)->str:
        return f"en: {self.phrase_en} | ru: {self.phrase_ru}"

