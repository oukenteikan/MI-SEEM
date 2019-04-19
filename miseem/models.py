from django.db import models

# Create your models here.

class System(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return self.name

class Sentence(models.Model):
    belong_to_system = models.ForeignKey('System', on_delete=models.DO_NOTHING)
    content = models.TextField()

    def __str__(self):
        return self.content