from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100, null=False)
    lyric = models.TextField(null = False)
    written_by = models.CharField(max_length=50, null=False)

    def __str__(self):
        return 'Song (title: {self.title},written_by: {self.written_by})'.format(self=self)

    def save_song(self):
        self.save()

    def delete_song(self):
        self.delete()

    @classmethod
    def search_song(cls,search_term):
        song = cls.objects.filter(title__icontains=search_term) | cls.objects.filter(lyric__icontains=search_term) | cls.objects.filter(written_by__icontains=search_term)
        return song