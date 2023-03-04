from django.db import models
import uuid
from django.utils import timezone

class Flashcard(models.Model):
    #id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    word = models.CharField(verbose_name='単語',max_length=40)
    description=models.CharField(verbose_name='説明',max_length=200)
    