from django.db import models

# Create your models here.
class Mezmur(models.Model):
    title = models.CharField(max_length=100, null=False)
    lyrics = models.TextField(null = False)
    written_by = models.CharField(max_length=50, null=False)

    def __str__(self):
        return 'Mezmur (title: {self.title},written_by: {self.written_by})'.format(self=self)

    def save_mezmur(self):
        self.save()

